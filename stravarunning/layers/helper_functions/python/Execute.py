from Data import getDataDict
from datetime import datetime
from StravaApi import StravaAPI
from FormattingUtils import Formatter

class Helper:
    def __init__(self):
        self.st = StravaAPI()
        self.format = Formatter()

    def getLatestActivity(self):
        return self.st.getLastSavedRun()

    def getOldActivity(self, id):
        try:
            data_dict = getDataDict()
            today_formatted_date = datetime.today().strftime("%d/%m/%y")
            old_date, Id = data_dict.get(today_formatted_date, 0)
            data = self.st.getActivityById(activity_id=Id)
            return data if data else None
        except Exception as e:
            print(f"Error Fetching Old Activity Data: {e}")
            return None

    def formatMessage(self, data):
        new = self.getLatestActivity()
        old = self.getOldActivity(id)
        new_message = self.format.formatStravaActivityHtml2(activity_data=new)
        old_message = (self.format.formatStravaActivityHtml2(activity_data=old) if old else None)
        old_message = old_message.replace("<h1>Strava Activity Summary</h1>","<h3>Similar Run from Last Streak</h3>") if old_message else ""
        return new_message + old_message
