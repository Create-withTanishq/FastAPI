from fastapi import FastAPI,Depends
from . import schemas ,models
from . database import engine ,SessionLocal
from sqlalchemy.orm import Session
 
app = FastAPI()

models.Base.metadata.create_all(engine)

#to convert to session format
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@app.post("/blog")
def create_blog(request : schemas.blog , db : Session = Depends(get_db) ):
    
    new_blog = models.Blog(title = request.title , body = request.body)
    
    #add it to the session
    db.add(new_blog)
    
    #commit the transaction to save it to db
    db.commit()
    
    #refreshing the db to get new id
    db.refresh(new_blog)
    
    return {
        "message" : "creating",
        "blog_id" : new_blog.id,
        "title" : new_blog.title,
        "body" : new_blog.body,
    }
    



