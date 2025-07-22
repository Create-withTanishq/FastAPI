| Topic                           | `db.delete(obj)`                    | `db.query().filter().delete(synchronize_session=False)` |
| ------------------------------- | ----------------------------------- | ------------------------------------------------------- |
| 🔁 Works with ORM instance?     | ✅ Yes (you load it first)           | ❌ No need to load it                                    |
| ⚡ Speed                         | ❌ Slower (because it loads objects) | ✅ Faster (direct SQL)                                   |
| 🧠 Keeps session state in sync? | ✅ Yes                               | ⚠️ No (you must manually know it’s deleted)             |
| 💥 Risk                         | Safe, but slow for big deletes      | Risky if your session still uses the deleted object     |
| 🧱 Use case                     | Fine for small-scale deletes        | Best for bulk deletes or APIs                           |
