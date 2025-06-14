from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

class LogData(BaseModel):
    soil_moisture: int

def map_range(x: int, in_max: int, out_max: int) -> int:
  return x * out_max // in_max

@app.post("/log/")
def log(log_data: LogData):
    file_test = "sensor_data/output.txt"

    cur_time = datetime.now().replace(microsecond=0).isoformat()
    
    normalized_soil_moisture = map_range(log_data.soil_moisture, 1023, 100) / 100
    
    with open(file_test, "a+") as f:
        f.write(f"soil moisture percentage at {cur_time} is {normalized_soil_moisture}\n")
    return {"status": "logged"}

@app.get("/")
def root():
    return {"message": "Hello World"}