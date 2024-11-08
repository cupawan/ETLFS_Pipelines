import os
import yaml
import pytz
# import folium
# import polyline
import requests
from stravalib.client import Client
from datetime import datetime, timedelta
from DatetimeUtils import CommonUtils


class StravaAPI:
    def __init__(self, config_path=None):
        # self.token_file = "strava_tokens.yaml"
        # self.access_token, self.refresh_token = self.loadTokens()
        self.access_token = os.environ["StravaAccessToken"]
        self.refresh_token = os.environ["StravaRefreshToken"]
        self.client = self.setUpClient()
        # self.ensureValidToken()
        self.utils = CommonUtils()
        self.ist = pytz.timezone('Asia/Kolkata')

    def setUpClient(self):
        client = Client()
        client.access_token = self.access_token
        return client

    def getAuthorizationUrl(self):
        authorization_url = (
            f"https://www.strava.com/oauth/authorize"
            f"?client_id={os.environ['StravaClientId']}"
            f"&response_type=code"
            f"&redirect_uri={os.environ['StravaRedirectUri']}"
            f"&scope=read,activity:read_all,activity:write"
            f"&approval_prompt=force"
        )
        return authorization_url

    def exchangeCodeForToken(self, code):
        try:
            response = requests.post(
                'https://www.strava.com/oauth/token',
                data={
                    'client_id': os.environ['StravaClientId'],
                    'client_secret': os.environ['StravaClientSecret'],
                    'code': code,
                    'grant_type': 'authorization_code'
                }
            )
            response.raise_for_status()
            tokens = response.json()
            self.access_token = tokens['access_token']
            self.refresh_token = tokens['refresh_token']
            self.saveTokens()
            self.client.access_token = self.access_token
        except requests.RequestException as e:
            print(f"Error exchanging code for token: {e}")

    def saveTokens(self):
        tokens = {
            'access_token': self.access_token,
            'refresh_token': self.refresh_token
        }
        with open(self.token_file, 'w') as f:
            yaml.safe_dump(tokens, f)

    def loadTokens(self):
        if os.path.exists(self.token_file):
            with open(self.token_file) as f:
                tokens = yaml.safe_load(f)
                return tokens.get('access_token'), tokens.get('refresh_token')
        return None, None

    def refreshAccessToken(self):
        try:
            response = requests.post(
                'https://www.strava.com/oauth/token',
                data={
                    'client_id': os.environ['StravaClientId'],
                    'client_secret': os.environ['StravaClientSecret'],
                    'grant_type': 'refresh_token',
                    'refresh_token': self.refresh_token,
                }
            )
            response.raise_for_status()
            tokens = response.json()
            self.access_token = tokens['access_token']
            self.refresh_token = tokens['refresh_token']
            self.client.access_token = self.access_token
            self.saveTokens()
        except requests.RequestException as e:
            print(f"Error refreshing access token: {e}")

    def ensureValidToken(self):
        if not self.access_token:
            print("Go to the following URL to authorize the application:")
            print(self.getAuthorizationUrl())
            authorization_code = input("Enter the authorization code from the URL: ").strip()
            self.exchangeCodeForToken(authorization_code)
        else:
            self.client.access_token = self.access_token

    def getOutputDict(self):
        return {
            'ID': [],
            'Date': [],
            'Name': [],
            'Distance': [],
            'Average Pace': [],
            'Max Pace': [],
            'Average Heart Rate': [],
            'Max Heart Rate': [],
            'Average Cadence': [],
            'Moving Time': [],
            'Comments': []
        }
    
    def getLastSavedActivity(self):
        try:
            headers = {
                'Authorization': f'Bearer {self.access_token}'
            }
            response = requests.get('https://www.strava.com/api/v3/athlete/activities', headers=headers)
            response.raise_for_status()
            return response.json()[0]
        except Exception as e:
            print(f"Error fetching all activities: {e}")
            self.refreshAccessToken()
            return self.getLastSavedActivity()
    
    def getActivityById(self, activity_id):
        try:
            headers = {
                'Authorization': f'Bearer {self.access_token}'
            }
            response = requests.get(f'https://www.strava.com/api/v3/activities/{activity_id}', headers=headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching activity by ID: {e}")
            self.refreshAccessToken()
            return self.getActivityById(activity_id)
    
    # def getActivityMap(self, activity_id, save_directory):
    #     try:
    #         data = self.getActivityById(activity_id=activity_id)
    #         polyline_encoded = data['map']['polyline']
    #         coordinates = polyline.decode(polyline_encoded)
    #         mymap = folium.Map(location=coordinates[0], zoom_start=16)
    #         folium.PolyLine(coordinates, color="red").add_to(mymap)
    #         mymap.fit_bounds(coordinates)
    #         mymap.save(save_directory)
    #         return True
    #     except Exception as e:
    #         print(f"Error fetching activity map: {e}")
    #         self.refreshAccessToken()
    #         return self.getActivityMap(activity_id, save_directory)
        
    def getYesterdayActivity(self, type = "Run"):
        before, after = datetime.today(), datetime.today() - timedelta(days=2)
        try:
            headers = {
                'Authorization': f'Bearer {self.access_token}'
            }

            params = {
                'before' : before,
                'after' : after
            }
                
            response = requests.get(f'https://www.strava.com/api/v3/activities/', headers=headers, params = params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching activity by ID: {e}")
            self.refreshAccessToken()
            # return self.getYesterdayActivity()

    def getActivitiesInDateRange(self, after, before):
        before = datetime.strptime(before, "%Y-%m-%d")
        after = datetime.strptime(after, "%Y-%m-%d")
        epoch_before = int(before.timestamp())
        epoch_after = int(after.timestamp())
        try:
            headers = {
                'Authorization': f'Bearer {self.access_token}'
            }

            params = {
                'before' : epoch_before,
                'after' : epoch_after
            }
                
            response = requests.get(f'https://www.strava.com/api/v3/activities/', headers=headers, params = params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching activity by ID: {e}")
            self.refreshAccessToken()
            return self.getActivitiesInDateRange(self, after, before)
        
    def getLastSavedRun(self):
        try:
            headers = {
                'Authorization': f'Bearer {self.access_token}'
            }
            response = requests.get('https://www.strava.com/api/v3/athlete/activities', headers=headers)
            response.raise_for_status()
            last = [i for i in response.json() if i['type'] == "Run"][0]
            return last
        except Exception as e:
            print(f"Error fetching all activities: {e}")
            self.refreshAccessToken()
            return self.getLastSavedRun()

