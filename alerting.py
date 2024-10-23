def check_alert_thresholds(weather_data, threshold_temp=35):
    alerts = []
    for entry in weather_data:
        if entry['temp'] > threshold_temp:
            alerts.append(f"Alert: Temperature in {entry['city']} exceeded {threshold_temp}°C")
    return alerts
