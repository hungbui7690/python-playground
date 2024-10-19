''' 
	Open Weather API
	- https://openweathermap.org/api
		# Geocoding API -> API Doc


'''

import requests
from rich import print_json


geo_url = 'http://api.openweathermap.org/geo/1.0/direct'
weather_url = "https://api.openweathermap.org/data/2.5/forecast"
key = '28d4883cb180676d90561d43c5caa22f'


# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
def get_geo_location(city, state):
	geo_params = {
		'q': city,
		'appid': key # API key -> in python, key will be in params object
	}
	response = requests.get(geo_url, params=geo_params)
	return response.json()


def main():
	coords = get_geo_location('broomfield', 'co')[0]
	print(coords)
	return


if __name__ == "__main__":
    main()
