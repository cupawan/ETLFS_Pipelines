import os
import pytz
import datetime
import logging
from collections import defaultdict
from TelegramUtils import TelegramMessage
from GarminConnectApi import GarminAPI
from FormattingUtils import Formatter
from EmailUtils import SendEmail
from MongoDbUtils import MongoUtils
from ErrorHandling import *

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

class Helper:
    def __init__(self):
        ist = pytz.timezone('Asia/Kolkata')
        self.sync_date = datetime.datetime.today().astimezone(ist).strftime('%d/%m/%y')
        self.this_hour = datetime.datetime.today().astimezone(ist).strftime('%H')
        self.tg = TelegramMessage()
        self.garmin_instance = GarminAPI()
        self.mongo_instance = MongoUtils()
        self.format_instance = Formatter()
        self.chat_id = os.environ['TelegramChatId']
        self.type_statistics_dict = defaultdict(
            lambda: (
                self.garmin_instance.getSleepStats,
                self.format_instance.sleep_html,
                f"{os.environ['ApplicationName']}_{os.environ['SourceName']}_sleep_insights"
                ),
            {
            os.environ['RunHour']: (
                self.garmin_instance.getRunningData,
                self.format_instance.running_html,
                f"{os.environ['ApplicationName']}_{os.environ['SourceName']}_running_insights"
                )
            }
            )
        
    def send_data(self):
        try:
            logger.info("Fetching data from GarminAPI")
            data = self.type_statistics_dict[self.this_hour][0]()
            html_body = self.type_statistics_dict[self.this_hour][1](data)
            collection_name = self.type_statistics_dict[self.this_hour][2]
            data_type = collection_name.split("_")[-2].title()
            logger.info("Data fetched successfully. Formatting email body.")
            email_body = Formatter().garminMainEmailFormatter(data = data, html_body = html_body)
            logger.info("Sending email with Garmin Insights")
            email_message = SendEmail(is_html=True).send_email(send_to = os.environ['RecEmail'], subject = f"Garmin {data_type} Insights", email_body = email_body)
            logger.info("Inserting Data into MongoDB")
            insert_data_in_mongo = self.mongo_instance.insert_records(collection_name= collection_name, data=data)
            logger.info(f"Inserted records in MongoDB:\n{insert_data_in_mongo}")
        except Exception as e:
            logger.error(str(e))
            raise NoDataError(msg=str(e))
