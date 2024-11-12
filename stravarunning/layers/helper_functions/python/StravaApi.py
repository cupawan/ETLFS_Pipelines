import os
import pytz
import logging
import requests
from stravalib.client import Client
from datetime import datetime, timedelta
from DatetimeUtils import CommonUtils

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

class StravaAPI:
    def __init__(self, config_path=None):
        self.access_token = os.environ["StravaAccessToken"]
        self.refresh_token = os.environ["StravaRefreshToken"]
        self.client = self.setUpClient()
        self.utils = CommonUtils()
        self.ist = pytz.timezone('Asia/Kolkata')
        
    def setUpClient(self):
        client = Client()
        client.access_token = self.access_token
        return client        

    def updateEnvironmentTokens(self):
        os.environ["StravaAccessToken"] = self.access_token
        os.environ["StravaRefreshToken"] = self.refresh_token

    def refreshAccessToken(self):
        response = requests.post(
            'https://www.strava.com/oauth/token',
            data={
                'client_id': os.environ['StravaClientId'],
                'client_secret': os.environ['StravaClientSecret'],
                'grant_type': 'refresh_token',
                'refresh_token': self.refresh_token,
            }
        )
        if response.status_code == 200:
            tokens = response.json()
            self.access_token = tokens['access_token']
            self.refresh_token = tokens['refresh_token']
            self.client.access_token = self.access_token
            self.updateEnvironmentTokens()
        else:
            logger.error(f"[Strava]: Code {response.status_code} {response.text}")
            raise NoDataError(code = response.status_code, msg = response.text)
                
    def getLastSavedActivity(self):
        try:
            headers = {
                'Authorization': f'Bearer {self.access_token}'
            }
            response = requests.get('https://www.strava.com/api/v3/athlete/activities', headers=headers)
            response.raise_for_status()
            return response.json()[0]
        except Exception as e:
            logger.warning(f"[Strava]: {response.status_code} {response.text}")
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
            logger.warning(f"[Strava]: {response.status_code} {response.text}")
            self.refreshAccessToken()
            return self.getActivityById(activity_id)
        
    def getYesterdayActivity(self, type = "Run"):
        before, after = datetime.today(), datetime.today() - timedelta(days=2)
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        params = {
            'before' : before,
            'after' : after
        }
            
        response = requests.get(f'https://www.strava.com/api/v3/activities/', headers=headers, params = params)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"[Strava]: Code {response.status_code} {response.text}")
            raise NoDataError(code = response.status_code, msg = response.text)
        
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

