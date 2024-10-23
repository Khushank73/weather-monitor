import requests

API_KEY = 'your_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def fetch_weather_data():
    weather_data = []
    for city in CITIES:
        params = {'q': city, 'appid': API_KEY}
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            weather_data.append({
                'city': city,
                'main': data['weather'][0]['main'],
                'temp': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'timestamp': data['dt']
            })
        else:
            print(f"Failed to fetch data for {city}: {response.status_code}")
    return weather_data
