from flask import Flask, render_template, request
from data_retrieval import fetch_weather_data
from data_processing import kelvin_to_celsius, calculate_daily_summary
from database import init_db, store_weather_data, store_daily_summary
from alerting import check_alert_thresholds
from visu import generate_daily_summary_plot
from database import add_city_column_to_daily_summary

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    city = request.form.get('city', 'Hyderabad')  # Default to Hyderabad if no city is selected
    weather_data = fetch_weather_data()

    # Filter data for the selected city and convert temperature to Celsius
    weather_data = [entry for entry in weather_data if entry['city'] == city]
    for entry in weather_data:
        entry['temp'] = kelvin_to_celsius(entry['temp'])

    store_weather_data(weather_data)
    daily_summary = calculate_daily_summary(weather_data)
    store_daily_summary(daily_summary, city)  # Store the summary in the database with the city
    alerts = check_alert_thresholds(weather_data)

    # Generate the plot for the selected city
    generate_daily_summary_plot(city)

    return render_template('index.html', daily_summary=daily_summary, alerts=alerts, city=city)

if __name__ == '__main__':
    init_db()
    add_city_column_to_daily_summary()  # Ensure city column is added to the daily_summary table
    app.run(debug=True)
