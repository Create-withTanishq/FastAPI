# secure password management
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes = ["bcrypt"] , deprecated = "auto")

class Hash():
    def bcrypt(password : str):
        return pwd_cxt.hash(password)
    
    def verify(entered_password : str , db_password : str):
        return pwd_cxt.verify(entered_password ,db_password)
    
