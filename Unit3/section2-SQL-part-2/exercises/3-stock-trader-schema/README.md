## Stock trader schema

Create a schema for the following application, a mock stock trader.

There are accounts. Accounts have
```
username
password_hash
balance
first_name
last_name
email_address
```

An account can make trades and hold positions in stocks.

An account will have many trades and many positions. A trade has one account,
a position has one account.

A position has the following information:

```
ticker
shares
```

A trade has the following information:

```
ticker
volume
unit_price
time
```

You will need to decide how foreign keys are arranged.

Create a `schema.py` file that generates this database.
