#cerating a post method
from fastapi import FastAPI 
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/")
def get_homepage():
    return {
        "message": "This is the homepage!"
    }

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = False  # added default value

@app.post("/blog")
def create_blog(blog: Blog):
    return {
        "message": "Blog is created!",
        "Blog info": {
            "Blog title": blog.title,
            "Blog body": blog.body,
            "Blog published": blog.published,
        }
    }
    
