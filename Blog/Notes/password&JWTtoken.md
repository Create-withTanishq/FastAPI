
---

### 📄— Password Hashing & JWT Authentication in FastAPI

---

## 🔐 PASSWORD HASHING & JWT TOKEN AUTHENTICATION — FASTAPI

---

### 📌 OBJECTIVE

To implement secure user authentication using:

* **Password hashing** with `passlib`
* **JWT token generation** with `python-jose`
* **Secure login flow** using FastAPI

---

## 🛠️ REQUIREMENTS

Make sure these are installed:

```bash
pip install passlib[bcrypt] python-jose python-dotenv
```

---

## 1️⃣ PASSWORD HASHING

### ✅ Why Hash?

Storing raw passwords is insecure. We hash them so:

* Even if the DB is leaked, passwords aren’t readable.
* Hashing is one-way (you can’t decode it back).

### 🔧 File: `hashing.py`

```python
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    def verify(plain_password: str, hashed_password: str):
        return pwd_cxt.verify(plain_password, hashed_password)
```

---

## 2️⃣ STORE HASHED PASSWORD (During Signup)

During user registration, hash the password before saving to DB:

```python
hashed_password = Hash.bcrypt(user.password)
```

---

## 3️⃣ JWT TOKEN GENERATION

### ✅ What is JWT?

* A **JSON Web Token** is a secure, tamper-proof string used to identify users.
* You generate it when the user logs in, and attach it to requests.

---

### 🔧 File: `JWTtoken.py`

```python
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta, timezone
from jose import jwt

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")  # Store in `.env`
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
```

---

## 4️⃣ LOGIN WORKFLOW

### 🔧 File: `authentication.py`

```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, JWTtoken
from ..database import get_db
from ..hashing import Hash

router = APIRouter(prefix="/login", tags=["authentication"])

@router.post("/")
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.user_email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid username. Sign up instead!"
        )

    if not Hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid password!"
        )

    access_token = JWTtoken.create_access_token(data={"sub": user.email})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
```

---

## 5️⃣ ENVIRONMENT VARIABLES

### 🔧 File: `.env`

```
SECRET_KEY=f3a4e99d8339289b4e0fa0a9b1e6d6b8.....
```

> ⚠️ NEVER hardcode your secret key in Python files. Keep it in `.env` and add `.env` to `.gitignore`.

---

## 🧠 WORKFLOW SUMMARY

```
[User Login Form] 
    ↓
[POST /login]
    ↓
[DB Check → User exists?]
    ↓
[Password Hash Verification]
    ↓
[JWT Token Creation]
    ↓
[Return token to user]
    ↓
[Client uses token in Authorization header for further requests]
```

---

## ✅ Example Token Response

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR...",
  "token_type": "bearer"
}
```

---

Let me know if you'd like to include **how to protect routes using this token** (`OAuth2PasswordBearer`, etc.) next.
