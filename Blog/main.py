from fastapi import FastAPI,Depends,status,HTTPException
from . import schemas ,models 
from . database import engine ,SessionLocal
from . hashing import Hash
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
    

@app.post("/blog" ,status_code= status.HTTP_201_CREATED, tags= ["Blog"])  #reponse code should 201 for created
def create_blog(request : schemas.blogBase , db : Session = Depends(get_db) ):
    
    new_blog = models.Blog(title = request.title , body = request.body ,user_id = 1) #for now harcoding user id
    
    #add it to the session
    db.add(new_blog)
    
    #commit the transaction to save it to db
    db.commit()
    
    #refreshing the db to get new id
    db.refresh(new_blog)
    
    return {
        "message" : "creating",
        "blog_id" : new_blog.id,
        "user_id" : new_blog.user_id,
        "title" : new_blog.title,
        "body" : new_blog.body,
    }
     
    
#getting all blogs from database
@app.get("/blog",  tags= ["Blog"])
def get_allBlogs(db : Session = Depends(get_db) ):
    blogs = db.query(models.Blog).all()
    return blogs
    
    

@app.get("/blog/{id}",response_model= schemas.showBlogs ,status_code= status.HTTP_200_OK,  tags= ["Blog"])
def get_blog(id : int , db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    #handeling exceptions
    if not blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND ,
                            detail= f"Blog with {id} not found !")
    return blog

# deleting a blog
@app.delete("/blog/{id}", status_code= status.HTTP_204_NO_CONTENT , tags= ["Blog"])
def delete_blog(id : int  , db : Session = Depends(get_db)):
    blog_to_del= db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog_to_del:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                            detail= f"Blog with id : {id} not found !")
    db.delete(blog_to_del)
    
    # alternative way:
    # db.query(models.Blog).filter(models.Blog.id == {id}).delete(synchronize_session= false)
    
    db.commit() #saving changes
    return

# updating ablog with particular id
@app.put("/blog/{id}" ,status_code= status.HTTP_202_ACCEPTED,  tags= ["Blog"])
def update_blog(request : schemas.blogBase , id : int , db : Session = Depends(get_db),):
    update_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not update_blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND ,
                        detail= f"Blog with id : {id} not found !")
    
    update_blog.title = request.title
    update_blog.body = request.body
    
    db.commit()
    db.refresh(update_blog)
    
    return {
        "message" : "Succcessfully Updated",
        "updated blog title" : update_blog.title,
        "updated blog body" : update_blog.body,
    }

@app.post("/user",response_model= schemas.showUser , tags= ["Users"])
def create_user(request : schemas.user , db : Session = Depends(get_db)):
    new_user = models.User(
        name = request.name,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/user/",response_model=schemas.showUser, tags= ["Users"])
def get_user(email : str , db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= f"User with email : '{email}' not found !")
    return user
    
    
    
     