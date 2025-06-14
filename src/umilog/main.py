from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

class LogData(BaseModel):
    soil_moisture: int

@app.post("/log/")
def log(log_data: LogData):
    file_test = "sensor_data/output.txt"

    cur_time = datetime.now().replace(microsecond=0).isoformat()
    
    normalized_soil_moisture = log_data.soil_moisture / 100
    
    with open(file_test, "a+") as f:
        f.write(f"soil moisture percentage at {cur_time} is {normalized_soil_moisture}\n")
    return {"status": "logged"}

@app.get("/")
def root():
    return {"message": "Hello World"}