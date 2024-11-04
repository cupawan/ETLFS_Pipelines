import requests
from boto3_toolkit import Boto3Utils


class OpenWeatherMap:
    def __init__(self):
        self.config = Boto3Utils().get_secret(secret_name= "WeatherPipelineSecrets")
        
    def geocode(self, address, limit=1):
        params = {'q': address, 'limit' : limit, 'appid' : self.config['OPENWEATHERMAP_API_KEY']}
        response = requests.get(url=self.config["OPENWEATHERMAP_GEOCODE_BASE_URL"],params = params).json()[0]
        data = [address, response['lat'], response['lon']]
        self.save_csv(data=data)
        return response['lat'], response['lon']
    
    def getWeatherData(self,lat,lon):
        try:
            params = {'lat': lat, 'lon' : lon, 'appid' : self.config['OPENWEATHERMAP_API_KEY'],'units' : 'metric'}
            response = requests.get(url = self.config["OPENWEATHERMAP_CURRENT_WEATHER_BASE_URL"],params=params)
            if response.status_code == 200:
                data = response.json()
                return data                        
            else:
                print("RESPONSE CODE: ",response.status_code)
                return None
        except Exception as e:
            print(f"Error while getting weather data: {str(e)}")
            return None
