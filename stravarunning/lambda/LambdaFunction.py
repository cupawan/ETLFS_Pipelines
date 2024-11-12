import os
import logging
import traceback
from Execute import Helper
from EmailUtils import SendEmail
from TelegramUtils import TelegramMessage
from ErrorHandling import *

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

sub = "Strava Run Statistics"



def LambdaHandler(event, context):
    help = Helper()
    telegram_instance = TelegramMessage()
    try:
        data = help.getLatestActivity()
        msg = help.formatMessage(data = data)
        SendEmail(is_html=True).send_email(send_to = os.environ["RecEmail"], subject = sub, email_body = msg)
    
    except NoDataError as e:
        error_message = (
            f"{e.msg}\n\n{str(e)}\n\nTraceback:\n{traceback.format_exc()}"
        )
        logger.error(error_message)
        telegram_instance.send_plain_message(
            chat_id=os.environ["TelegramChatId"], text= error_message
        )
        return {"statusCode": 404, "body": error_message}
    
    except Exception as e:
        error_message = (
            f"An error occurred: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
        )
        logger.error(error_message)
        telegram_instance.send_plain_message(
            chat_id=os.environ["TelegramChatId"], text=error_message
        )
        return {"statusCode": 404, "body": error_message}