from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def get_homepage():
    return {"message status" : "received" ,
            "data" : {
                "name" : "Tanishq",
                "date" : datetime.now().date(),
                "time" : datetime.now().time(),
            }}

