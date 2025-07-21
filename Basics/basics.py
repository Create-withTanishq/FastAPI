from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

#path operation decorator
@app.get("/")

#path operation function
def get_homepage():
    return {"message status" : "received" ,
            "data" : {
                "name" : "Tanishq",
                "date" : datetime.now().date(),
                "time" : datetime.now().time(),
            }}
    
    
#static routing should be above dynamic routing with same path
@app.get("/blog/unpublished")
def get_unpublished_blogs():
    return{
        "message" : "Data recived",
        "blogs" : "unpublished blogs",
    }
    
    
#dynamic routing
@app.get("/blog/{id}")
def show(id : int):
    return{"id" : id}
