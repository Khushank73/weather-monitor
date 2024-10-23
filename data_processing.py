def kelvin_to_celsius(kelvin_temp):
    return round(kelvin_temp - 273.15, 2)

def calculate_daily_summary(weather_data):
    if not weather_data:
        return {
            'average_temp': 0,
            'max_temp': 0,
            'min_temp': 0,
            'dominant_weather': 'N/A'
        }

    daily_summary = {
        'average_temp': sum(d['temp'] for d in weather_data) / len(weather_data),
        'max_temp': max(d['temp'] for d in weather_data),
        'min_temp': min(d['temp'] for d in weather_data),
        'dominant_weather': max(set(d['main'] for d in weather_data), key=lambda x: [d['main'] for d in weather_data].count(x))
    }
    return daily_summary
