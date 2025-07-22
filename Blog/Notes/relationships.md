---

# 📘 Notes on Relationships in FastAPI with SQLAlchemy

---

## 🧩 1. Why Relationships?

When working with databases, **relationships** let us connect tables together.
In FastAPI with SQLAlchemy, we often need to:

* Associate each blog with a user (author)
* Fetch all blogs written by a user
* Enable navigation between related data models

---

## 🧱 2. Our Models: `User` and `Blog`

We want to build a **One-to-Many** relationship:

> One `User` can write **many** `Blogs`
> But each `Blog` belongs to **one** `User`

---

## 👇 Model Definitions

```python
class Blog(Base):
    __tablename__ = "Blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    
    # This is the foreign key - links Blog to a specific User by ID
    user_id = Column(Integer, ForeignKey("Users.id"))
    
    # Create the relationship from Blog → User
    author = relationship("User", back_populates="blogs")
```

```python
class User(Base):
    __tablename__ = "Users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
    # This allows us to access all blogs by a user
    blogs = relationship("Blog", back_populates="author")
```

---

## 📌 3. Important Concepts

### ✅ `ForeignKey("Users.id")`

* Points from `Blog.user_id` to `Users.id`
* Links the **Blog table** to the **User table**
* Must match the actual **table name**, not the class name!

---

### ✅ `relationship(...)`

* Used in both models to define **bi-directional navigation**
* `relationship("User")` allows accessing the user (author) of a blog
* `relationship("Blog")` allows accessing all blogs written by a user

---

### ✅ `back_populates=...`

* Makes the relationship **two-way**
* Ensures both `User.blogs` and `Blog.author` stay in sync
* Required on **both sides** of the relationship

---

## 🔄 4. Relationship Flow Diagram

```
User (1) ───────────< Blog (Many)
            id        user_id (FK)
            👇             👆
        blogs[]     blog.author
```

---

## ✨ 5. Sample Usage

### 🔹 Accessing all blogs from a user

```python
user = db.query(User).filter(User.id == 1).first()
print(user.blogs)  # List of all blogs authored by this user
```

### 🔹 Accessing blog's author

```python
blog = db.query(Blog).filter(Blog.id == 10).first()
print(blog.author.name)  # Name of the user who wrote the blog
```

---

## ✅ Summary

| Term             | Purpose                                        |
| ---------------- | ---------------------------------------------- |
| `ForeignKey()`   | Creates a link between two tables              |
| `relationship()` | Establishes Python-side access to related rows |
| `back_populates` | Keeps both ends of relationship in sync        |
| `user.blogs`     | List of all blogs by the user                  |
| `blog.author`    | User who wrote the blog                        |

---
