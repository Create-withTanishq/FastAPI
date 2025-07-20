from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return{"message" : "EV connected !"}


ev_data = []

@app.post("/ev/reports")
def post_ev_status(vehicle_id : str , battery : float,  lon : float , lat : float): 
    ev_status = {
        "vehicle_id" : vehicle_id,
        "battery" : battery,
        "time" : datetime.now(),
        "location" : {"lat" : lat, "lon" : lon},
    }
    ev_data.append(ev_status)
    return {"message" : "Data Received" , "Data" : ev_status}
    
    
@app.get("/ev/{vehicle_id}")
def get_ev_status(vehicle_id: str):
    for ev in ev_data:
        if ev["vehicle_id"] == vehicle_id:
            return ev
    return {"error": "Vehicle not found"}


