import sqlite3 


CREATE_SQL = """
CREATE TABLE artwork(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    title VARCHAR(255),
    artist VARCHAR(225),
    year_made DATE,
    medium VARCHAR(64),
    price FLOAT);

CREATE TABLE artist(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    first VARCHAR(255),
    last VARCHAR(255),
    style VARCHAR(64),
    birthplace VARCHAR(255),
    dob DATE);

CREATE TABLE typesofart(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    group VARCHAR(255),
    artwork_id INTEGER,
    artist_id INTEGER,
    FOREIGN KEY (`artwork_id`) REFERENCES artwork(id),
    FOREIGN KEY (`artist_id) REFERENCES artist(id));
"""

DROP_SQL = "DROP TABLE IF EXISTS artgallery"

with sqlite3.connect("artgallery.db") as conn:
    cursor = conn.cursor() # cursor executes statements, connect connects the statements
    cursor.execute(DROP_SQL) # deletes table: accounts if already exists
    cursor.execute(CREATE_SQL)

# to run this 
# python3 schema.py ----- run schema
# sqlite3 accounts.db ---- interactive w accounts.db
# .schema
# if you try to create it again ... "table accounts already exists" so we added DROP_SQL
