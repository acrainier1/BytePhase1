import sqlite3

CREATE_SQL = """
CREATE TABLE accounts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_num INTEGER NOT NULL,
    pin VARCHAR(4),
    first VARCHAR(225),
    last VARCHAR(225),
    balance FLOAT);
"""

DROP_SQL = "DROP TABLE IF EXISTS accounts;"

with sqlite3.connect("account.db") as conn:
    cursor = conn.cursor()

    cursor.execute(DROP_SQL)

    cursor.execute(CREATE_SQL)

def insert_account(**kwargs):
    account_num = kwargs.get("account_num")
    pin = kwargs.get("pin")
    first = kwargs.get("first")
    last = kwargs.get("last")
    balance = kwargs.get("balance", 0.0)
    # never do this
    BAD_INSERT_SQL = f"""
INSERT INTO accounts(account_num, pin, first, last, balance)
VALUES ({account_num}, '{pin}', '{first}', '{last}', {balance});
"""

    INSERT_SQL = """
INSERT INTO accounts(account_num, pin, first, last, balance)
VALUES (:account_num, :pin, :first, :last, :balance);"""

    values = {
        "account_num": account_num,
        "pin": pin,
        "first": first,
        "last": last,
        "balance": balance
    }

    with sqlite3.connect("account.db") as conn:
        cursor = conn.cursor()
        print(INSERT_SQL)
        # second argument is a dictionary with keys corresponing
        # to the named insertion points in the query you wrote
        cursor.execute(INSERT_SQL, values)


def update_row(id, **kwargs):
    account_num = kwargs.get("account_num")
    pin = kwargs.get("pin")
    first = kwargs.get("first")
    last = kwargs.get("last")
    balance = kwargs.get("balance")

    UPDATE_SQL = f"""
        UPDATE accounts
        SET account_num=?, pin=?, first=?, last=?, balance=?
        WHERE id=?"""

    with sqlite3.connect("account.db") as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE_SQL, (account_num, pin, first, last, balance, id))

    
def delete_row(id):
    DELETE_SQL = f"""DELETE FROM accounts WHERE id=?;"""
    with sqlite3.connect("account.db") as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE_SQL, (id,))


def print_table():
    SELECT_SQL = """ SELECT * FROM accounts; """
    with sqlite3.connect("account.db") as conn:
        conn.row_factory = sqlite3.Row # cause .fetch methods to return rows
                                        # as dictionary-like objects rather
                                        # than list
        cursor = conn.cursor()
        cursor.execute(SELECT_SQL)
        rows = cursor.fetchall()

        for row in rows:
            print(dict(row))

        SELECT_SQL = """ SELECT * FROM accounts WHERE id=1; """
        cursor.execute(SELECT_SQL)
        rows = cursor.fetchone()
        if row is not None:
            print(dict(row))
        else:
            print("row is None")

        LOGIN_SQL = """ SELECT * FROM accounts WHERE account_num=:account_num, pin=:pin """
        cursor.execute(LOGIN_SQL, {"account_num": 12345, "pin": "1234"})
        rows = cursor.fetchall()

insert_account(first='Mike', last='Bloom', account_num='123456', pin='1234', balance=3.5)
insert_account(first='Carter', last='Adams', account_num='999999', pin='9999', balance=20.0)
update_row(2, first='Carter2', last='Adams2', account_num='999992', pin='9992', balance=2.0)
delete_row(1)
# insert_account(pin="Robert'); DROP TABLE accounts;")


