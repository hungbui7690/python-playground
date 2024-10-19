''' 
	Open Weather API
	- https://openweathermap.org/api
		# Geocoding API -> API Doc
		# 5 Day / 3 Hour Forecast -> API Doc


'''

import requests
from rich import print_json


geo_url = 'http://api.openweathermap.org/geo/1.0/direct'
weather_url = "https://api.openweathermap.org/data/2.5/forecast"
key = '28d4883cb180676d90561d43c5caa22f'


def get_geo_location(city, state):
    geo_params = {
      'q': city,
      'appid': key 
    }
    response = requests.get(geo_url, params=geo_params)
    return response.json()


# https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
def get_forecast(lat, lon):
	weather_params = {
		'lat': lat,
		'lon': lon,
		'appid': key
	}

	response = requests.get(weather_url, params=weather_params)
	return response.json()


def main():
	coords = get_geo_location('broomfield', 'co')[0]
	print(coords)
	forecast = get_forecast(coords['lat'], coords['lon'])

	print_json(data=forecast)
	print(len(forecast['list']))

	return


if __name__ == "__main__":
    main()
