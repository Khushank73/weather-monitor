import sqlite3

def init_db():
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    
    # Create the weather_data table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS weather_data (
                    id INTEGER PRIMARY KEY,
                    city TEXT,
                    main TEXT,
                    temp REAL,
                    feels_like REAL,
                    timestamp INTEGER
                )''')
    
    # Create the daily_summary table with city information
    c.execute('''CREATE TABLE IF NOT EXISTS daily_summary (
                    id INTEGER PRIMARY KEY,
                    city TEXT,
                    date TEXT,
                    average_temp REAL,
                    max_temp REAL,
                    min_temp REAL,
                    dominant_weather TEXT
                )''')
    
    conn.commit()
    conn.close()

def add_city_column_to_daily_summary():
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    
    # Check if the city column exists, if not, add it
    c.execute("PRAGMA table_info(daily_summary);")
    columns = [col[1] for col in c.fetchall()]
    
    if 'city' not in columns:
        c.execute("ALTER TABLE daily_summary ADD COLUMN city TEXT")
    
    conn.commit()
    conn.close()

def store_weather_data(data):
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    
    for entry in data:
        c.execute('''INSERT INTO weather_data (city, main, temp, feels_like, timestamp)
                     VALUES (?, ?, ?, ?, ?)''', (entry['city'], entry['main'], entry['temp'], entry['feels_like'], entry['timestamp']))
    
    conn.commit()
    conn.close()

def store_daily_summary(summary, city):
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    
    c.execute('''INSERT INTO daily_summary (city, date, average_temp, max_temp, min_temp, dominant_weather)
                 VALUES (?, ?, ?, ?, ?, ?)''', 
                 (city, 'today', summary['average_temp'], summary['max_temp'], summary['min_temp'], summary['dominant_weather']))

    conn.commit()
    conn.close()
