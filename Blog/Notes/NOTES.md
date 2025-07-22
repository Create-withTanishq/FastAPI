
---

### 📄 `NOTES.md` – FastAPI + SQLAlchemy Blog API 

---

# 🚀 FastAPI Blog API – Starter Project

This is a step-by-step backend API using **FastAPI** + **SQLAlchemy** + **Pydantic** to create a simple blog system.

---

## 📦 Project Structure

```
.
├── main.py             # Main app with FastAPI routes
├── database.py         # DB connection and session maker
├── models.py           # SQLAlchemy models (DB tables)
├── schemas.py          # Pydantic schemas (request validation)
├── blog.db             # SQLite DB file (auto-created)
└── NOTES.md           # You're reading it 😉
```

---

## 💡 Core Concepts Covered

| Tool           | Purpose                                            |
| -------------- | -------------------------------------------------- |
| **FastAPI**    | Web API framework                                  |
| **Pydantic**   | Data validation using `BaseModel`                  |
| **SQLAlchemy** | ORM for defining and interacting with the database |
| **SQLite**     | Lightweight database stored locally as `blog.db`   |

---

## 🔧 `database.py` – Setup Database Engine & Sessions

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"  # No space after /// !

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
```

### ✅ What it does:

* Connects to an SQLite DB file: `blog.db`
* Creates `SessionLocal` to manage DB sessions
* `Base` is the parent class for defining table models

---

## 🧱 `models.py` – Define DB Table with SQLAlchemy

```python
from .database import Base
from sqlalchemy import Column, Integer, String

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
```

### ✅ What it does:

* Defines the structure of the `blogs` table
* `Blog` object ↔ one row in the database

---

## 📋 `schemas.py` – Define Request Schema with Pydantic

```python
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str
```

### ✅ What it does:

* Used to **validate** incoming JSON payloads
* Ensures title and body are required strings

---

## 🚀 `main.py` – Build the API Routes

```python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import schemas, models
from .database import engine, SessionLocal

app = FastAPI()
models.Base.metadata.create_all(engine)
```

### 🧠 Creating a DB Session per Request:

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

### 📝 POST `/blog` – Create a New Blog

```python
@app.post("/blog")
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {
        "message": "creating",
        "blog_id": new_blog.id,
        "title": new_blog.title,
        "body": new_blog.body,
    }
```

### ✅ Flow:

1. User sends JSON → validated by `schemas.Blog`
2. DB session is injected via `Depends(get_db)`
3. A new `Blog` object is created and added
4. `.commit()` saves it to the DB
5. `.refresh()` pulls the generated ID
6. JSON response is returned

---

## ✅ Run the App

In your terminal:

```bash
uvicorn main:app --reload
```

Then go to:

* 🌐 [http://localhost:8000/docs](http://localhost:8000/docs) → for Swagger UI
* 🌐 [http://localhost:8000/redoc](http://localhost:8000/redoc) → for ReDoc

---

## 🧠 Key Notes

* `models.py` → for defining DB tables
* `schemas.py` → for validating incoming requests
* `database.py` → for creating DB engine and sessions
* `main.py` → connects everything and runs API logic

---

## 🔄 Example Request (via Swagger UI or Postman)

### Endpoint:

```
POST /blog
```

### Request Body:

```json
{
  "title": "FastAPI is awesome",
  "body": "Loving the learning journey!"
}
```

### Response:

```json
{
  "message": "creating",
  "blog_id": 1,
  "title": "FastAPI is awesome",
  "body": "Loving the learning journey!"
}
```

---

## 🧱 Next Steps You Can Add

* [ ] Add a `GET /blog/{id}` endpoint
* [ ] Add error handling for non-existent blog IDs
* [ ] Add DELETE and UPDATE methods
* [ ] Migrate from SQLite to MySQL/PostgreSQL
* [ ] Connect to a frontend using API calls (e.g., Framer, React, ESP32)

---

You're not just coding, you're building backend brains 🧠⚙️
Happy coding, engineer! 💡🚀

---
