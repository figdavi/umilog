# TODO: 
# - add readme
# - check commits for sensitive data
# - upload to github (public)

from fastapi import FastAPI, HTTPException
from umilog.database import create_sensor_table, log_sensor_data
from pydantic import BaseModel

class SensorData(BaseModel):
    raw_soil_moisture: int

MAX_SOIL_MOISTURE = 1023
create_sensor_table()
app = FastAPI()

def format_soil_moisture(raw_soil_moisture: int) -> float:
    """Normalizes and inverts the range of the raw soil moisture value, 
    since 0 means wet and 1023 means dry

    Args:
        raw_soil_moisture (int): raw soil moisture data

    Returns:
        float: formatted soil moisture data
    """    
    return round(1 - (raw_soil_moisture / MAX_SOIL_MOISTURE), 2)

@app.post("/log")
def log_route(sensor_data: SensorData):
    soil_moisture = format_soil_moisture(sensor_data.raw_soil_moisture)
    try:
        log_sensor_data(soil_moisture)
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Failed to log data: {err}")

    return {"status": "logged"}

@app.get("/")
def root():
    return {"message": "Hello World"}