from fastapi import APIRouter,Depends, HTTPException, status
from .. import schemas , models, JWTtoken
from .. database import get_db
from sqlalchemy.orm import Session
from .. hashing import Hash

router = APIRouter(
    prefix = "/login",
    tags = ["authentication"]
)

@router.post("/")
def login(request : schemas.login , db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.user_email).first()
    if not user :
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Invalid username , Sign up instead !!"
        )
    if not Hash.verify(request.password , user.password):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Invalid Credentials"
        )
    #generate jwt token
    access_token = JWTtoken.create_access_token(data={"sub" : user.email})
    return {
        "access_token" : access_token,
        "token_type" : "bearer"
    }