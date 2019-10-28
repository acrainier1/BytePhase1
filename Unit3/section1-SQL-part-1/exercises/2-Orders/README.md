## Order tracker

Think of a business that would have need to track customer orders.

It needs to have an order id that is distinct from the database row id.

It needs to keep track of when an order was made. Look up the information on
SQLite3's field types and how there is not a DATETIME field. There are various
strategies for storing time as a string or number. In this author's opinion,
storing the Unix timestamp of a given time (the thing returned by time.time(),
the number of seconds since Jan 1 1970) is the best way to go.

What other information would you need to keep track of for this business? A
restaurant and a long-haul trucking company would need different fields.

Write a setup.py that creates your table and INSERTs a few sample values.

Write an operations.py that has functions that has functions that can:

    * Create an order

    * Update an order, perhaps marking a "shipped" column.

    * Delete an order

    * Print an attractive table of all orders
