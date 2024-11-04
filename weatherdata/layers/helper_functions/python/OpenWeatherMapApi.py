import os
import requests


class OpenWeatherMap:
    def __init__(self):
        self.api_key = os.environ['OWMApiKey']
        self.geocode_base_url = os.environ['OWMGeocodeBaseUrl']
        self.current_weather_base_url = os.environ['OWMCurrentWeatherBaseUrl']
        
        
    def geocode(self, address, limit=1):
        params = {'q': address, 'limit' : limit, 'appid' : self.api_key}
        response = requests.get(url=self.geocode_base_url,params = params).json()[0]
        data = [address, response['lat'], response['lon']]
        self.save_csv(data=data)
        return response['lat'], response['lon']
    
    def getWeatherData(self,lat,lon):
        try:
            params = {'lat': lat, 'lon' : lon, 'appid' : self.api_key,'units' : 'metric'}
            response = requests.get(url = self.current_weather_base_url,params=params)
            if response.status_code == 200:
                data = response.json()
                return data                        
            else:
                print("RESPONSE CODE: ",response.status_code)
                return None
        except Exception as e:
            print(f"Error while getting weather data: {str(e)}")
            return None
