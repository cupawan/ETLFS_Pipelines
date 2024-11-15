import logging
from Data import getDataDict
from datetime import datetime
from StravaApi import StravaAPI
from FormattingUtils import Formatter

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

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
            logger.info(f"[Strava]: Today's Date: {today_formatted_date}")
            old_date, Id = data_dict.get(today_formatted_date, 0)
            logger.info(f"[Strava]: Last Streak Date: {old_date}")
            data = self.st.getActivityById(activity_id=Id)
            return data if data else None
        except Exception as e:
            print(f"Error Fetching Old Activity Data: {e}")
            return None

    def formatMessage(self, data):
        new = self.st.getLastSavedRun()
        old = self.getOldActivity(id)
        new_message = self.format.formatStravaActivityHtml2(activity_data=new)
        logger.info(f"[Strava]: Formatted message for Latest Run Successfully")
        old_message = (self.format.formatStravaActivityHtml2(activity_data=old) if old else None)
        old_message = old_message.replace("Strava Activity Summary","Similar Run from Last Streak") if old_message else ""
        logger.info(f"[Strava]: Formatted message for Last Streak Run Successfully")
        return new_message + old_message
