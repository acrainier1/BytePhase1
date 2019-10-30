import sqlite3 


CREATE_SQL = """
CREATE TABLE account(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username VARCHAR(32),
    password_hash VARCHAR(255),
    balance FLOAT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email_address VARCHAR(128));

CREATE TABLE position(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    ticker VARCHAR(16),
    shares FLOAT),
    account_id INTEGER,
    FOREIGN KEY (`account_id) REFERENCES account(id));

CREATE TABLE trade(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    position_id INTEGER,
    ticker VARCHAT(16),
    volume INTEGER,
    unit_price FLOAT,
    time DATE,
    account_id INTEGER,
    FOREIGN KEY (`position_id`) REFERENCES position(id),
    FOREIGN KEY (`ticker`) REFERENCES position(ticker), ???????????????
    FOREIGN KEY (`account_id) REFERENCES account(id));
"""

DROP_SQL = "DROP TABLE IF EXISTS stocktrader"

with sqlite3.connect("stocktrader.db") as conn:
    cursor = conn.cursor() # cursor executes statements, connect connects the statements
    cursor.execute(DROP_SQL) # deletes table: accounts if already exists
    cursor.execute(CREATE_SQL)