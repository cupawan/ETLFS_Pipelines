import os
import pytz
import logging
import requests
from datetime import datetime, timedelta
from DatetimeUtils import CommonUtils
from ErrorHandling import *


logger = logging.getLogger(__name__)
logger.setLevel("INFO")

class StravaAPI:
    def __init__(self):
        self.access_token = os.environ["StravaAccessToken"]
        self.utils = CommonUtils()
        self.ist = pytz.timezone('Asia/Kolkata')
        self.headers = {'Authorization': f'Bearer {self.access_token}'}
        self.base_url = "https://www.strava.com/api/v3"
        self.activities_url = f"{self.base_url}/athlete/activities"
    
    def getLastSavedActivity(self):
        response = requests.get(self.activities_url, headers= self.headers)
        if response.status_code == 200:
            return response.json()[0]
        else:
            logger.error(f"[Strava]: Code {response.status_code} {response.text}")
            raise NoDataError(code = response.status_code, msg = response.text)
    
    def getActivityById(self, activity_id):
        response = requests.get(f'{self.base_url}/activities/{activity_id}', headers= self.headers)
        if response.status_code == 200:
            return response.json()[0]
        else:
            logger.error(f"[Strava]: Code {response.status_code} {response.text}")
            raise NoDataError(code = response.status_code, msg = response.text)
        
    def getYesterdayActivity(self, type = "Run"):            
        response = requests.get(
            f'{self.base_url}/activities/',
            headers= self.headers,
            params = {'before' : datetime.today(), 'after' : datetime.today() - timedelta(days=2)}
            )
        if response.status_code == 200:
            return response.json()[0]
        else:
            logger.error(f"[Strava]: Code {response.status_code} {response.text}")
            raise NoDataError(code = response.status_code, msg = response.text)

    def getActivitiesInDateRange(self, after, before):
        before = datetime.strptime(before, "%Y-%m-%d")
        after = datetime.strptime(after, "%Y-%m-%d")
        response = requests.get(
            f'{self.base_url}/activities/',
            headers= self.headers,
            params = {'before' : int(before.timestamp()),'after' : int(after.timestamp())}
            )
        if response.status_code == 200:
            return response.json()[0]
        else:
            logger.error(f"[Strava]: Code {response.status_code} {response.text}")
            raise NoDataError(code = response.status_code, msg = response.text)
        
    def getLastSavedRun(self):
        response = requests.get(self.activities_url, headers=self.headers)
        last = [i for i in response.json() if i['type'] == "Run"][0]
        if response.status_code == 200:
            return last
        else:
            logger.error(f"[Strava]: Code {response.status_code} {response.text}")
            raise NoDataError(code = response.status_code, msg = response.text)
