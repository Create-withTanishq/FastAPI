from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./Blog/blog.db"


engine = create_engine(url= SQLALCHEMY_DATABASE_URL, connect_args= {"check_same_thread" : False})

SessionLocal = sessionmaker(bind = engine , autoflush= False , autocommit = False)

Base = declarative_base()

#to convert to session format
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()