| SQLAlchemy Command                       | What it Does                                              | Example Use                        |
| ---------------------------------------- | --------------------------------------------------------- | ---------------------------------- |
| `db.query(Model).all()`                  | Returns **all rows** from the table                       | Get all blogs                      |
| `db.query(Model).first()`                | Returns the **first row** or `None`                       | Get first blog                     |
| `db.query(Model).filter(...).first()`    | Filter with a condition and return first matching row     | Get blog with ID = 1               |
| `db.query(Model).filter(...).all()`      | Filter with condition and return all matching rows        | Get all blogs by a certain user    |
| `db.add(obj)`                            | Adds a new instance (row) to the session                  | Add a new blog                     |
| `db.commit()`                            | Commits the current transaction                           | Save blog to DB                    |
| `db.refresh(obj)`                        | Refreshes an instance to get generated fields (like `id`) | Get latest DB info                 |
| `db.delete(obj)`                         | Marks the object for deletion from DB                     | Delete blog                        |
| `db.rollback()`                          | Rolls back the current transaction if there's an error    | Cancel changes due to failure      |
| `db.query(Model).get(primary_key_value)` | Shortcut to get an object by primary key                  | `db.query(User).get(1)`            |
| `filter(Model.column == value)`          | SQL WHERE condition                                       | `filter(User.name == "Tanu")`      |
| `filter(Model.column.like("%word%"))`    | SQL LIKE query                                            | Search for title containing a word |
| `order_by(Model.column.desc())`          | Order by descending column value                          | Sort blogs by newest               |
| `order_by(Model.column.asc())`           | Order by ascending                                        | Sort by title A–Z                  |
| `limit(n)`                               | Limit number of rows returned                             | Get top 5 blogs                    |
| `offset(n)`                              | Skip `n` rows                                             | Pagination                         |
| `exists().where(...)`                    | Check if a row exists matching a condition                | Useful for validations             |
| `join(OtherModel)`                       | SQL JOIN between two tables                               | Blog joined with User              |
| `relationship("OtherModel")` in Model    | Setup SQLAlchemy relationship for auto join               | Blog belongs to a user             |
| `Column(..., nullable=False)`            | Column must not be null                                   | Enforce required fields            |
| `Column(..., unique=True)`               | No duplicate values allowed                               | Unique email/usernames             |
| `Column(..., default=value)`             | Set default value if none provided                        | Default publish status             |
| `Base.metadata.create_all(bind=engine)`  | Creates DB tables based on models                         | Usually done once on app start     |
