from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas ,models 
from sqlalchemy.orm import Session
from .. database import get_db
from .. hashing import Hash

router = APIRouter(
    tags=["users"]
)



@router.post("/user",response_model= schemas.showUser , )
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



@router.get("/user/",response_model=schemas.showUser, )
def get_user(email : str , db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= f"User with email : '{email}' not found !")
    return user
    