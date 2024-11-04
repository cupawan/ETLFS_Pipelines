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
        self.telegram_docname = f"/tmp/GarminStatistics_{datetime.datetime.today().astimezone(ist).strftime('%d_%m_%y')}.html"
        self.tg = TelegramMessage()
        self.chat_id = os.environ['TelegramChatId']

    def _send_telegram_doc(self, html_body):
        logger.info("Writing HTML body to file for Telegram document")
        with open(self.telegram_docname, 'w') as f:
            f.write(html_body)        
        logger.info("Sending document message via Telegram")
        self.tg.send_document_message(document_file_path=self.telegram_docname, chat_id=self.chat_id, caption="Today's Garmin Statistics")        
        logger.info(f"Removing temporary file: {self.telegram_docname}")
        os.remove(self.telegram_docname)
    
    def _send_telegram_text(self, msg_body):       
        logger.info("Sending text message via Telegram")
        self.tg.send_plain_message(text = msg_body, chat_id=self.chat_id)
        

    def send_data(self):
        logger.info("Initializing GarminAPI and MongoUtils instances")
        garmin_instance = GarminAPI()
        mongo_instance = MongoUtils()
        logger.info("Fetching data from GarminAPI")
        sleep_data = garmin_instance.getSleepStats()
        body_stats_data = garmin_instance.getYesterdayBodyStats()
        running_data, metadata, activity_id = garmin_instance.getRunningData()
        map_url = garmin_instance.getMapImage(activity_id)
        streak, day_flag = garmin_instance.getRunningStreak()
        metadata.update({"mapUrl": map_url})
        metadata.update({"streak": streak})
        r_html = Formatter().running_html(running_data=running_data, metadata=metadata)
        s_html = Formatter().sleep_html(sleep_data=sleep_data)
        b_html = Formatter().body_stats_html(body_stats_data=body_stats_data)
        if sleep_data and body_stats_data and running_data:
            logger.info("All data fetched successfully. Formatting email body.")
            email_body = Formatter().garminMainEmailFormatter(running_html=r_html, sleep_html=s_html, body_stats_html=b_html, metadata=metadata)
            logger.info("Sending email with Garmin statistics")
            email_message = SendEmail(is_html=True).send_email(body=email_body, subject="Garmin Statistics")
            # self._send_telegram_doc(html_body=email_body)
            logger.info("Updating MongoDB with Garmin status")
            write_in_mongo = mongo_instance.update_record(
                collection_name='garmin_status',
                query={'isUpdated': True},
                update_data={'date': self.sync_date, 'isUpdated': True},
                upsert=True
            )
            logger.info(f"Updated status in MongoDB: {write_in_mongo}")
            logger.info("Inserting sleep data into MongoDB")
            insert_sleep_data_in_mongo = mongo_instance.insert_records(collection_name="garmin_sleep_statistics", data=sleep_data)
            logger.info("Inserting body stats data into MongoDB")
            insert_bodystats_data_in_mongo = mongo_instance.insert_records(collection_name="garmin_body_statistics", data=body_stats_data)
            logger.info("Inserting running data into MongoDB")
            insert_running_data_in_mongo = mongo_instance.insert_records(collection_name="running", data=running_data)
            logger.info(f"Inserted records in MongoDB:\n Sleep Data: {insert_sleep_data_in_mongo}\n Body Statistics: {insert_bodystats_data_in_mongo}\n Running Data: {insert_running_data_in_mongo}")
        else:
            msg = f"No Data Received: Running - {bool(running_data)}, Sleep Statistics - {bool(sleep_data)}, Body Statistics - {bool(body_stats_data)}"
            logger.warning(msg)
            self.tg.send_plain_message(chat_id=self.chat_id, text=msg)
            
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
