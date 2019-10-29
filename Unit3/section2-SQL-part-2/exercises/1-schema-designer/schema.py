import sqlite3 

CREATE_SQL = """
CREATE TABLE teacher(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    first VARCHAR(255),
    last VARCHAR(255),);

CREATE TABLE student(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    first VARCHAR(255),
    last VARCHAR(255),);

CREATE TABLE class(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    subject VARCHAR(64);
    teacher VARCHAR(255),);
    """

DROP_SQL = "DROP TABLE IF EXISTS snack"

with sqlite3.connect("school.db") as conn:
    cursor = conn.cursor() # cursor executes statements, connect connects the statements
    cursor.execute(DROP_SQL) # deletes table: accounts if already exists
    cursor.execute(CREATE_SQL)

# to run this 
# python3 schema.py ----- run schema
# sqlite3 accounts.db ---- interactive w accounts.db
# .schema
# if you try to create it again ... "table accounts already exists" so we added DROP_SQL
