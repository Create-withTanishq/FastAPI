from . database import Base
from sqlalchemy import Column , String , Integer , ForeignKey
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = "Blogs"
    id = Column(Integer , primary_key= True , index= True)
    title = Column(String)
    body = Column(String)
    
    # Foreign key takes *table name not *class name
    user_id = Column(Integer,ForeignKey("Users.id"))  
    author = relationship("User" , back_populates= "blogs")

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key= True ,index= True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
    blogs = relationship("Blog", back_populates= "author")
     