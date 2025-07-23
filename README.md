
# CSV to SQLite Importer

A simple and functional Python script that **converts `.csv` files into a table in a SQLite3 database**, automatically inferring the data types of each column.

## Features

- Automatic connection to a `.db` SQLite database
- Table creation based on the `.csv` header
- Automatic data type inference (`INTEGER`, `REAL`, `TEXT`)
- Data insertion into the table
- Optional commit confirmation

---

## How to Use

1. **Clone the repository** or copy the `main.py` file.

2. Run with Python 3:

```bash
python main.py
```

3. The script will prompt for:

- Path to the `.csv` file
- Path (or name) of the `.db` file

Example:
```
Path to csv file => students.csv
Path to db file => my_database.db
```

4. It will create a table named `students` and insert the CSV data into it.

5. You can confirm or cancel the insert before the final commit.

---

## Example Input

### File `students.csv`:

```csv
name,age,grade
Ana,20,8.5
Bruno,22,7.8
Carlos,21,9.0
```

### Generated SQL table:

```sql
CREATE TABLE students (
  name TEXT,
  age INTEGER,
  grade REAL
)
```

---

## Project Structure

```
.
├── main.py
└── students.csv
```

---

## How It Works

- **Type Inference:** Based on the 2nd row of the CSV, the script tries to convert the data to `int`, `float`, or keeps it as `str`.
- **Table Name:** Generated from the name of the CSV file.
- **SQL Commands:** Automatically built from the columns and inferred types.

---

## Requirements

- Python 3.x
- No external libraries (only `sqlite3` and `csv` from the standard library)

---
