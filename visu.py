import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import matplotlib.pyplot as plt
import sqlite3
from flask import current_app

def generate_daily_summary_plot(city):
    with current_app.app_context():  # Ensure we are in the app context
        conn = sqlite3.connect('weather_data.db')
        c = conn.cursor()
        
        # Fetch data for the selected city
        c.execute('SELECT date, average_temp, max_temp, min_temp FROM daily_summary WHERE city = ?', (city,))
        data = c.fetchall()
        
        if not data:
            conn.close()
            return

        dates = [row[0] for row in data]
        avg_temps = [row[1] for row in data]
        max_temps = [row[2] for row in data]
        min_temps = [row[3] for row in data]

        # Plot the data
        plt.figure(figsize=(10, 5))
        plt.plot(dates, avg_temps, label='Average Temp')
        plt.plot(dates, max_temps, label='Max Temp')
        plt.plot(dates, min_temps, label='Min Temp')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.legend()
        plt.title(f'Daily Weather Summary for {city}')
        plt.xticks(rotation=45)
        
        # Save the plot in the static folder
        plt.savefig('static/plots/daily_summary.png')
        plt.close()

        conn.close()
