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
    
    
# pydantic model for response_model : show_users
class showUser(BaseModel):
    name : str
    email : str
    class config():
        orm_mode = True
        
    