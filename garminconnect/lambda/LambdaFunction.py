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

def LambdaHandler(event, context):
    logger.info(f"Starting Execution")
    help = Helper()
    try:
        help.send_data()
        return {"statusCode": 200, "body": "OK"}
    except NoDataError as e:
        logger.error(e.msg)
        telegram_instance.send_plain_message(chat_id=os.environ["TelegramChatId"], text= e.msg)
        return {"statusCode": 404, "body": e.msg}
    except Exception as e:
        error_message = (f"An error occurred: {str(e)}\n\Traceback:\n{traceback.format_exc()}")
        logger.error(error_message)
        telegram_instance.send_plain_message(chat_id=os.environ["TelegramChatId"], text=error_message)
        return {"statusCode": 404, "body": error_message}
