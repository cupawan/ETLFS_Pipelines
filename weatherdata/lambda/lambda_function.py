import logging
from OpenWeatherMapApi import OpenWeatherMap
from EmailUtils import SendEmail
from MongoDbUtils import MongoUtils
from FormattingUtils import Formatter


logger = logging.getLogger(__name__)
logger.setLevel("INFO")

def lambda_handler(event,context):
    contacts = MongoUtils().find_one(collection_name='weather_pipeline_contacts', key = 'Status', value = 'Activated')
    owm = OpenWeatherMap()
    email_ = SendEmail(is_html=True)
    contacts = list(contacts) if not isinstance(contacts,list) else contacts
    for contact in contacts:
        weather_data = owm.getWeatherData(lat = contact['Coordinates'][0],lon = contact['Coordinates'][1])
        if weather_data:            
            message_table = Formatter().formatWeatherDataHtmlTableEmail(data_list=weather_data['daily'][0],
                                                            day_list= weather_data['hourly'][0:25], 
                                                            name = contact['Name'],
                                                            location = contact['Location'])                                    
            send = email_.send_email(send_to=contact['Email'], subject="Today's Weather Forecast", email_body = message_table)            
            logger.info(f"Email {send['status']} to {contact['Name']}")
        