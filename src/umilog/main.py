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
    
    with open(file_test, "a+") as f:
        f.write(f"soil_moisture at {cur_time} is {log_data.soil_moisture}\n")
    return {"status": "logged"}

@app.get("/")
def root():
    return {"message": "Hello World"}