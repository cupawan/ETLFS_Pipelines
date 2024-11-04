import os
import json
import logging
import traceback
from Execute import Helper
from MongoDbUtils import MongoUtils
from TelegramUtils import TelegramMessage
from ErrorHandling import *

logger = logging.getLogger(__name__)
logger.setLevel("INFO")


telegram_instance = TelegramMessage()
mongo_instance = MongoUtils()

def main():
    help = Helper()
    status_mongo = mongo_instance.find_one(collection_name = 'garmin_status', query = {'date': help.sync_date,'isUpdated': True})
    logger.info(f"Sync Status: {status_mongo}")
    if not status_mongo:
        logger.info(f"Starting Execution")
        help.send_data()
        logger.info("Process Completed")
        return {'statusCode': 200, 'status': "OK"}
    else:
        logger.info("Already Executed")              
        return {'statusCode': 200, 'status': "Already executed"}

def LambdaHandler(event, context):
    try:
        response = main()
        return {'statusCode': 200, 'body': json.dumps(response)}
    except (NoRunningError,NoSleepError,NoBodyStatsError) as e:
        logger.error(e.msg)
        telegram_instance.send_plain_message(chat_id=os.environ['TelegramChatId'], text=e.msg)
        return {'statusCode': 404, 'body': e.msg} 
    except Exception as e:
        error_message = f"An error occurred: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
        logger.error(error_message)
        telegram_instance.send_plain_message(chat_id=os.environ['TelegramChatId'], text=error_message)
        return {'statusCode': 404, 'body': error_message} 
    
