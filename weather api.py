import requests
import os
from datetime import datetime

user_api = os.environ['weather_data']
location = input('enter city name:').upper()

#from web api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

complete_api_link ="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(complete_api_link)
api_data = api_link.json()

weather_desc = api_data['weather'][0]['description']
temp = (api_data['main']['temp'])-273.35
formated_temp = "{:.2f}".format(temp)
hmdt = api_data['main']['humidity']
long = api_data['coord']['lon']
lat = api_data['coord']['lat']
country = api_data['sys']['country']
date_time = datetime.now().strftime("%d %b %Y| %I:%M:%S %p")

print('******** Weather information ********:')
print(f'{location},{country} on {date_time}')
print(f'longitude: {long} latitude: {lat}')
print('current temperature: ', formated_temp,'C')
print('current weather desc: ', weather_desc)
print('current Humidity: ', hmdt,'%')
