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
        self.refresh_token = os.environ["StravaRefreshToken"]
        self.auth_url = "https://www.strava.com/oauth/token"
        self.athlete_activities_url = "https://www.strava.com/api/v3/athlete/activities"
        self.activities_url = "https://www.strava.com/api/v3/activities"
        self.refreshAccessToken()
        self.access_token = os.environ["StravaAccessToken"]
        self.headers = {'Authorization': f'Bearer {self.access_token}'}
        self.utils = CommonUtils()
        self.ist = pytz.timezone('Asia/Kolkata')
             

    def updateEnvironmentTokens(self):
        os.environ["StravaAccessToken"] = self.access_token
        os.environ["StravaRefreshToken"] = self.refresh_token

    def refreshAccessToken(self):
        response = requests.post(self.auth_url, data={
            'client_id': os.environ['StravaClientId'],
            'client_secret': os.environ['StravaClientSecret'],
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token
            })
        if response.status_code == 200:
            tokens = response.json()
            self.access_token = tokens['access_token']
            self.refresh_token = tokens['refresh_token']
            self.updateEnvironmentTokens()
        else:
            msg = f"[Strava]: Code {response.status_code} {response.text}"
            raise NoDataError(code = response.status_code, msg = msg)
                
    def getLastSavedActivity(self):
        response = requests.get(self.athlete_activities_url, headers= self.headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            logger.warning(f"[Strava]: {response.status_code} {response.text}\n Refreshing Tokens")
            self.refreshAccessToken()
            return self.getLastSavedActivity()
        else:
            msg = f"[Strava]: Code {response.status_code} {response.text}"
            raise NoDataError(code = response.status_code, msg = msg)
                        
    def getActivityById(self, activity_id):
        response = requests.get(f'{self.activities_url}/{activity_id}', headers= self.headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            logger.warning(f"[Strava]: {response.status_code} {response.text}\n Refreshing Tokens")
            self.refreshAccessToken()
            return self.getActivityById(activity_id)
        else:
            msg = f"[Strava]: Code {response.status_code} {response.text}"
            raise NoDataError(code = response.status_code, msg = msg)
                   
    def getYesterdayActivity(self, type = "Run"):
        before, after = datetime.today(), datetime.today() - timedelta(days=2)
        response = requests.get(f'{self.activities_url}/', headers=self.headers, params = {'before' : before,'after' : after})
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            logger.warning(f"[Strava]: {response.status_code} {response.text}\n Refreshing Tokens")
            self.refreshAccessToken()
            return self.getYesterdayActivity()
        else:
            msg = f"[Strava]: Code {response.status_code} {response.text}"
            raise NoDataError(code = response.status_code, msg = msg)
        
    def getActivitiesInDateRange(self, after, before):
        epoch_before = int(datetime.strptime(before, "%Y-%m-%d").timestamp())
        epoch_after = int(datetime.strptime(after, "%Y-%m-%d").timestamp())            
        response = requests.get(f'{self.activities_url}/', headers=self.headers, params = {'before' : epoch_before, 'after' : epoch_after})
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            logger.warning(f"[Strava]: {response.status_code} {response.text}\n Refreshing Tokens")
            self.refreshAccessToken()
            return self.getActivitiesInDateRange(after, before)
        else:
            msg = f"[Strava]: Code {response.status_code} {response.text}"
            raise NoDataError(code = response.status_code, msg = msg)
        
    def getLastSavedRun(self):
        response = requests.get(self.athlete_activities_url, headers=self.headers)
        if response.status_code == 200:
            last = [i for i in response.json() if i['type'] == "Run"][0]
            return last
        elif response.status_code == 401:
            logger.warning(f"[Strava]: {response.status_code} {response.text}\n Refreshing Tokens")
            self.refreshAccessToken()
            return self.getLastSavedRun()
        else:
            msg = f"[Strava]: Code {response.status_code} {response.text}"
            raise NoDataError(code = response.status_code, msg = msg)
