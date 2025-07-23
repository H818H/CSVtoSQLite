import sqlite3
import csv


class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.con = None
        self.cursor = None

    def connect(self):
        self.con = sqlite3.connect(self.db_file)
        self.cursor = self.con.cursor()

    def execute(self, sql):
        if not self.cursor:
            raise RuntimeError("Database was not connected")
        self.cursor.execute(sql)

    def executemany(self, sql, params):
        if not self.cursor:
            raise RuntimeError("Database was not connected")
        self.cursor.executemany(sql, params)

    def commit(self):
        if self.con:
            self.con.commit()

    def close(self):
        if self.con:
            self.con.close()


def sqlite_types(val):
    if isinstance(val, int):
        return "INTEGER"
    elif isinstance(val, float):
        return "REAL"
    else:
        return "TEXT"


def get_types(val):
    try:
        return int(val)
    except ValueError:
        try:
            return float(val)
        except ValueError:
            return val


def get_table_name(csv_path):
    return csv_path.split("/")[-1].split(".")[0]


def get_list_values_from_table(csv_file):
    csv_raw_rows = []
    try:
        with open(csv_file, "r", encoding="utf-8") as fp:
            r = csv.reader(fp)
            for i in r:
                csv_raw_rows.append(i)
            return csv_raw_rows
    except FileNotFoundError:
        print(f"Error: {csv_file} not found")
        return None


def get_csv_data(csv_file):
    data = []
    with open(csv_file, "r", encoding="utf-8") as fp:
        file = csv.DictReader(fp)
        for i in file:
            data.append(dict(i))
        return data


def get_first_value_from_table(csv_data):
    return list(csv_data[1].values())


def get_inferred_types(val):
    inferred_types = []
    for i in val:
        t = get_types(i)
        inferred_types.append(t)
    return inferred_types


def create_table(db, table_name, inferred_types, header):
    sql_types = [sqlite_types(v) for v in inferred_types]

    columns = ", ".join([f"{col} {sqltype}" for col, sqltype in zip(header, sql_types)])

    sql = f"CREATE TABLE {table_name} ({columns})"

    db.execute(sql)


def insert_into_table(db, table_name, inferred_types, csv_raw_rows):
    placeholders = ", ".join(["?"] * len(inferred_types))
    params = [[get_types(val) for val in linha] for linha in csv_raw_rows[1:]]

    sql = f"INSERT INTO {table_name} VALUES ({placeholders})"

    db.executemany(sql, params)


def confirm_commits(db, header):
    confirm = input("Confirm changes (Y/N) =>")

    if confirm.lower() == "y":
        print(f"Header: {header}")
        db.commit()
    else:
        print("Returning to main! Commits weren't completed")


def main():
    while True:
        csv_file = input("Path to csv file =>")
        csv_raw_rows = get_list_values_from_table(csv_file)

        if csv_raw_rows:
            break
        else:
            continue

    db_file = input("Path to db file =>")
    db = Database(db_file)

    csv_dict_rows = get_csv_data(csv_file)

    header = list(csv_dict_rows[0].keys())

    first_row_values = get_first_value_from_table(csv_dict_rows)

    inferred_types = get_inferred_types(first_row_values)

    table_name = get_table_name(csv_file)

    db.connect()

    create_table(db, table_name, inferred_types, header)

    insert_into_table(db, table_name, inferred_types, csv_raw_rows)

    confirm_commits(db, header)

    db.close()


if __name__ == "__main__":
    main()
