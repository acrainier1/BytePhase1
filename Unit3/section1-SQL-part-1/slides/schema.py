import sqlite3

CREATE_SQL = """
CREATE TABLE accounts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_num INTEGER NOT NULL,
    pin VARCHAR(4),
    first VARCHAR(255),
    last VARCHAR(255),
    balance FLOAT);
"""

DROP_SQL = "DROP TABLE IF EXISTS accounts;"

with sqlite3.connect("accounts.db") as conn:
    cursor = conn.cursor()

    cursor.execute(DROP_SQL)

    cursor.execute(CREATE_SQL)

def insert_account(**kwargs):
    account_num = kwargs.get("account_num")
    pin = kwargs.get("pin")
    first = kwargs.get("first")
    last = kwargs.get("last")
    balance = kwargs.get("balance", 0.0)
    # never do this:
    BAD_INSERT_SQL = f"""
INSERT INTO accounts(account_num, pin, first, last, balance)
VALUES ({account_num}, '{pin}', '{first}', '{last}', {balance});
"""
    # sanitize your queries, this has automatic checking for
    # malicious values
    INSERT_SQL = """
INSERT INTO accounts(account_num, pin, first, last, balance)
VALUES (:account_num, :pin, :first, :last, :balance); """

    values = {
        "account_num": account_num,
        "pin": pin,
        "first": first,
        "last": last,
        "balance": balance
    }

    with sqlite3.connect("accounts.db") as conn:
        cursor = conn.cursor()
        # print(INSERT_SQL)
        # second argument is a dictionary with keys corresponding
        # to the named insertion points in the query you wrote
        cursor.execute(INSERT_SQL, values)

        newid = cursor.lastrowid
        print(f"the new id value for the inserted row is {newid}")

def update_row(id, **kwargs):
    # exercise for you
    pass

def delete_row(id):
    # exercise for you
    pass

def print_table():
    SELECT_SQL = """ SELECT * FROM accounts; """
    with sqlite3.connect("accounts.db") as conn:
        conn.row_factory = sqlite3.Row  # cause .fetch methods to return rows
                                        # as dictionary-like objects rather
                                        # than lists
        cursor = conn.cursor()
        cursor.execute(SELECT_SQL)
        rows = cursor.fetchall()

        for row in rows:
            print(dict(row))

        SELECT_SQL = """ SELECT * FROM accounts WHERE id=3; """
        cursor.execute(SELECT_SQL)
        row = cursor.fetchone()
        if row is not None:
            print(dict(row))
        else:
            print("row is None")

        LOGIN_SQL = """ SELECT * FROM accounts WHERE account_num=:account_num AND pin=:pin """

        cursor.execute(LOGIN_SQL, {"account_num": 123456, "pin": "1234"})
        logged_in_user = cursor.fetchone()

        if logged_in_user is None:
            print("could not log in")
        else:
            print("logged in\n", dict(logged_in_user))


insert_account(first='Mike', last='Bloom', account_num='123456', pin='1234', balance=3.5)
insert_account(first='Carter', last='Adams', account_num='999999', pin='9999', balance=-20.0)
print_table()

