from pydantic import BaseModel

#pydantic model
class blog(BaseModel):
    title : str
    body : str