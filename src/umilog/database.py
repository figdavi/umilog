from pathlib import Path
import sqlite3
from datetime import datetime

DB_FILE_NAME = 'sensor.sqlite3'
DATA_DIR = Path('/data')

DB_PATH = DATA_DIR / DB_FILE_NAME

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_sensor_table():
    with get_connection() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS sensor_data (
                        datetime TEXT,
                        soil_moisture REAL
                    )""")

def log_sensor_data(soil_moisture: float):
    """Inserts sensor data into the db

    Args:
        soil_moisture (float): soil moisture data being logged
    """    
    
    cur_datetime = datetime.now().replace(microsecond=0).isoformat()
    
    with get_connection() as conn:
        conn.execute("INSERT INTO sensor_data VALUES (?, ?)", 
                     (cur_datetime, soil_moisture))