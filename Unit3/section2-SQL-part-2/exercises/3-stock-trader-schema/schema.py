import sqlite3 


CREATE_SQL_ACCOUNT = """
CREATE TABLE account(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username VARCHAR(32) NOT NULL,
    password_hash VARCHAR(255),
    balance FLOAT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email_address VARCHAR(128));"""


CREATE_SQL_POSITION = """
CREATE TABLE position(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    ticker VARCHAR(16) NOT NULL,
    shares FLOAT,
    account_id INTEGER,
    FOREIGN KEY (`account_id`) REFERENCES account(id));"""


CREATE_SQL_TRADE = """
CREATE TABLE trade(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker VARCHAT(16) NOT NULL,
    volume INTEGER,
    unit_price FLOAT,
    time DATE,
    account_id INTEGER,
    FOREIGN KEY (`account_id`) REFERENCES account(id));"""

DROP_SQL = {"DROP_SQL_ACCOUNT": "DROP TABLE IF EXISTS account",
            "DROP_SQL_POSITION": "DROP TABLE IF EXISTS position",
            "DROP_SQL_TRADE": "DROP TABLE IF EXISTS trade"}

with sqlite3.connect("stocktrader.db") as conn:
    cursor = conn.cursor() # cursor executes statements, connect connects the statements  
    for k,v in DROP_SQL.items():
        cursor.execute(k) # deletes table: accounts if already exists
    cursor.execute(CREATE_SQL)