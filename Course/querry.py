from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_homepage():
    return {"message": "This is the homepage"}

#use of parameters
@app.get("/blog")
def published_blog(limit: int = 10, published: bool = True):
    if published:
        return {
            "blog type": "published",
            "blog max limit": limit
        }
    else:
        return {
            "blog type": "unpublished",
            "blog max limit": limit
        }
