from open_weather_map import OpenWeatherMap
from send_email import EmailWithPython
from mongo_utils import MongoUtils
from formatter1 import Formatter


def lambda_handler(event,context):
    contacts = MongoUtils().find_one(collection_name='weather_pipeline_contacts', key = 'Status', value = 'Activated')
    owm = OpenWeatherMap()
    email_ = EmailWithPython(is_html=True)
    contacts = list(contacts) if not isinstance(contacts,list) else contacts
    for contact in contacts:
        weather_data = owm.getWeatherData(lat = contact['Coordinates'][0],
                                          lon = contact['Coordinates'][1])
        if weather_data:
            # message = Formatter().formatWeatherDataHtmlEmail(data_list=weather_data['daily'][0],
            #                                                 day_list= weather_data['hourly'], 
            #                                                 name = contact['Name'],
            #                                                 location = contact['Location'])            
            message_table = Formatter().formatWeatherDataHtmlTableEmail(data_list=weather_data['daily'][0],
                                                            day_list= weather_data['hourly'][0:25], 
                                                            name = contact['Name'],
                                                            location = contact['Location'])                                    
            send = email_.send_email(send_to=contact['Email'], subject="Today's Weather Forecast", email_body = message_table)            
            print(f"Email {send['status']} to {contact['Name']}")
        