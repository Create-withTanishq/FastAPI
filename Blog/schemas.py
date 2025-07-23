from pydantic import BaseModel
from typing import List

# pydantic model for Blog
class blogBase(BaseModel):
    title : str
    body : str
    
class blog(blogBase):
    class config():
        orm_mode = True
    
# pydantic model for user
class user(BaseModel):
    name : str
    email : str
    password : str
    
    
# pydantic model for response_model : show_users
class showUser(BaseModel):
    name : str
    email : str
    blogs : List[blog]
    class config():
        orm_mode = True
        
# pydantic model for response_model : showing blogs
class showBlogs(BaseModel):
    title : str
    body : str
    author : showUser
    class config:
        orm_mode = True


# pydantic model for login
class login(BaseModel):
    username : str
    user_email : str
    password : str
    

# For JWT token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username : str | None = None

    