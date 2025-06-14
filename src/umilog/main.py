from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
from pathlib import Path

app = FastAPI()

class SensorData(BaseModel):
    soil_moisture: int

MAX_SOIL_MOISTURE = 1023

def format_soil_moisture(soil_moisture: int) -> float:
    """Normalizes and inverts the range of the soil moisture value, since 0 means wet and 1023 means dry

    Args:
        soil_moisture (int): raw soil moisture data

    Returns:
        float: formatted soil moisture
    """    
    return round(1 - (soil_moisture / MAX_SOIL_MOISTURE), 2)

@app.post("/log/")
def log(sensor_data: SensorData):
    file_test = "sensor_data/output.txt"
    
    Path(file_test).parent.mkdir(parents=True, exist_ok=True)
    

    cur_time = datetime.now().replace(microsecond=0).isoformat()
    
    formatted_soil_moisture = format_soil_moisture(sensor_data.soil_moisture)
    
    with open(file_test, "a+") as f:
        f.write(f"soil moisture percentage at {cur_time} is {formatted_soil_moisture}\n")
    return {"status": "logged"}

@app.get("/")
def root():
    return {"message": "Hello World"}