import os
import pytz
import datetime
import logging
from TelegramUtils import TelegramMessage
from GarminConnectApi import GarminAPI
from FormattingUtils import Formatter
from EmailUtils import SendEmail
from MongoDbUtils import MongoUtils
from Boto3Toolkit import Boto3Utils

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
        self.type_statistics_dict = {"12": (self.garmin_instance.getSleepStats, self.format_instance.sleep_html, "garmin_sleep_statistics"), "8": (self.garmin_instance.getRunningData, self.format_instance.running_html, "garmin_running_statistics")}
    
    def _send_telegram_text(self, msg_body):       
        logger.info("Sending text message via Telegram")
        self.tg.send_plain_message(text = msg_body, chat_id=self.chat_id)
        
    def send_data(self):
        logger.info("Fetching data from GarminAPI")
        data = self.type_statistics_dict[self.this_hour][0]()
        html_body = self.type_statistics_dict[self.this_hour][1](data)
        logger.info("Data fetched successfully. Formatting email body.")
        email_body = Formatter().garminMainEmailFormatter(data = data, html_body = html_body)
        logger.info("Sending email with Garmin statistics")
        email_message = SendEmail(is_html=True).send_email(send_to = os.environ['RecEmail'], subject = "Garmin Statistics", email_body = email_body)
        # self._send_telegram_doc(html_body=email_body)
        # logger.info("Updating MongoDB with Garmin status")
        # write_in_mongo = self.mongo_instance.update_record(collection_name='garmin_status', query={'isUpdated': True}, update_data={'date': self.sync_date, 'isUpdated': True},upsert=True)
        # logger.info(f"Updated sync status in MongoDB: {write_in_mongo}")
        logger.info("Inserting Data into MongoDB")
        collection_name = self.type_statistics_dict[self.this_hour][2]
        insert_data_in_mongo = self.mongo_instance.insert_records(collection_name= collection_name, data=data)
        logger.info(f"Inserted records in MongoDB:\n{insert_data_in_mongo}")
            
    def send_data_min(self):
        logger.info("Initializing GarminAPI and MongoUtils instances")
        garmin_instance = GarminAPI()
        logger.info("Fetching data from GarminAPI")
        sleep_data = garmin_instance.getSleepStats()
        running_data, metadata, activity_id = garmin_instance.getRunningData()
        streak, day_flag = garmin_instance.getRunningStreak()
        metadata.update({"streak": streak})
        r_text = Formatter().running_text(running_data=running_data, metadata=metadata)
        s_text = Formatter().sleep_text(sleep_data=sleep_data)
        if sleep_data and running_data:
            logger.info("All data fetched successfully. Formatting text body.")
            msg_body = f"{r_text}\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n{s_text}"
            logger.info("Sending telegram message with Garmin statistics")
            self._send_telegram_text(msg_body=msg_body)
        else:
            msg = f"No Data Received: Running - {bool(running_data)}, Sleep Statistics - {bool(sleep_data)}"
            logger.warning(msg)
            self.tg.send_plain_message(chat_id=self.chat_id, text=msg)
