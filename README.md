
# CSV to SQLite Importer (with argparse)

A command-line Python script that imports data from a `.csv` file into a SQLite3 database, **automatically inferring the data types** and allowing you to choose whether or not to confirm the commit.

## Features

- CLI interface using `argparse`
- Table creation based on CSV header
- Automatic data type inference (`INTEGER`, `REAL`, `TEXT`)
- Optional confirmation before committing changes
- Uses only Python's standard library

---

## How to Use

Run the script with:

```bash
python script.py --csv path/to/file.csv --db path/to/database.db
```

Optional flag:

- `--no-confirm`: skips the commit confirmation prompt and commits directly

### Example:

```bash
python script.py --csv students.csv --db school.db
```

Or without confirmation prompt:

```bash
python script.py --csv students.csv --db school.db --no-confirm
```

---

## Example CSV Input

### File `students.csv`:

```csv
name,age,grade
Ana,20,8.5
Bruno,22,7.8
Carlos,21,9.0
```

### Resulting SQL Table:

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
├── script.py
└── students.csv
```

---

## Requirements

- Python 3.x
- No external dependencies (uses `sqlite3`, `csv`, and `argparse` from the standard library)

---

## Author

Cauã Augusto  
Made for learning and practical usage of Python + SQLite via CLI.

---
