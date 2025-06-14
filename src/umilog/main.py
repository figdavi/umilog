from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

class SensorData(BaseModel):
    soil_moisture: int

MAX_SOIL_MOISTURE = 1023

def normalize_soil_moisture(soil_moisture: int) -> float:
  return soil_moisture / MAX_SOIL_MOISTURE

@app.post("/log/")
def log(sensor_data: SensorData):
    file_test = "sensor_data/output.txt"

    cur_time = datetime.now().replace(microsecond=0).isoformat()
    
    normalized_soil_moisture = normalize_soil_moisture(sensor_data.soil_moisture)
    
    with open(file_test, "a+") as f:
        f.write(f"soil moisture percentage at {cur_time} is {normalized_soil_moisture}\n")
    return {"status": "logged"}

@app.get("/")
def root():
    return {"message": "Hello World"}