from pydantic import BaseModel

# pydantic model for Blog
class blog(BaseModel):
    title : str
    body : str
    
# pydantic model for user
class user(BaseModel):
    name : str
    email : str
    password : str
    