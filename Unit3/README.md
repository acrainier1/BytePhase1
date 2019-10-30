# Python3: SQLite3 and MVC's

### Learning Objectives

* Connect a sqlite3 database to a python file
* Open and close connections to a database from a py file
* Build and import a seed file for testing data/code

---

### Context

* Yesterday we learned basic SQL CRUD commands. Now lets utilize these to help us keep persistent data.
* Along side persistent data, well complete our MVC application.

---

### Lesson

#### Part 1 - Recap of Yesterday and how does SQLite fall into our MVC app

* The concept of MVC is to write organized code
* Yesterday we worked on connecting two separate files. Each file with their specified purpose. `Views` and `Controllers`
* As we know the `Controller` holds the application logic so it not only talks to the view but also talks to the `Models` which interacts with the database

***Five Min Exercise***

* Draw the MVC diagram. Go from the browser to the database to the view
* Make a table for the CRUD operations and their translation to SQL syntax


#### Part 2 - Createdb.py

* Alright now we're going to make a file to create our database. 
* Yesterday we practiced all our SQL CRUD commands in the terminal
* Now we're going to import the sqlite3 module into a python file for use.

```
import sqlite3

conn = sqlite3.connect('databasename.db')

conn.execute(
	"""
	CREATE TABLE tablename (
		id INTEGER PRIMARY KEY, 
		character TEXT,
		movie TEXT,
		year INTEGER
	);
	"""
)

conn.commit()
conn.close()

print("Your database was created")
```
* `.connect("dbname.db")` allows us to connect to a database. 
	* If there is no database with that name, this command will automatically make one
	* We assign this connection to a variable called `conn` which we will use later
* `conn.execute` - we use the execute method from the sqlite3 module to run a SQL command in python. 
* `conn.close` will close the connection to the database
* The last print statement is there to give you some notification that everything ran smoothly. 
* The triple quotes are `doc strings` we can use these to write our SQL statements in multiple lines, and complete our statements with a semi-colon. This looks much nicer than writing everything on one line. 

***Five Min Exercise***

* create a createdb file
* Don't actually write code. just pseudo code. 
* What will the columns be in your table?
* What type of data will you need for your RPG game?
* At the end well come back and review what you have. 

---

* The point of this exercise is to plan out your database.
* We don't want to build incomplete databases.
* When working at a company you can't just "drop tables" and recreate them again. 
* Planning out your database is extremely important. Do this before writing any code

#### Part 3 - Seed.py

* So before we move over to our Models lets actually put something in our database that we can use to test. 
* This is called a seed file
* We only have to run this file ONCE when the data base is created
* This will be separate from our createdb file for now. 
* Once you get the hang of it feel free to combine the two.

```
"""
Seed your database with admins
"""

import sqlite3

db = 'mydb'

USERS = [
	["Anna Kendrick", "soulmate", "12345", "mylove@myheart.com", "[1234567,1234567,23455647]"],
	["Peter Parker", "spiderman", "12345", "parker@parker.com", "[1234563,23451234,234567]"]
]

conn = sqlite3.connect(db)
c = conn.cursor()

print("Destroying old data")
c.execute("DELETE FROM user")

for user in USERS:
	c.execute("""
		INSERT INTO user ("name", "username", "password", "email", "phone_num") VALUES (?, ?, ?, ?, ?)""",(user[0], user[1], user[2], user[3], user[4]))

conn.commit()

c.close()

print("Looks like we're all good")
```
* `.cursor()` - We need a cursor to travel through the database file. This is similar to having a cursor in a text file, or using the file I/O library.
* `.commit()` - You only use this on the manipulation of data in your DB
* `.close()` - closing your connection

***SANITIZE DATA***

* Notice the question marks in the example above. 
* This is known as sanitizing your data
* Everything inside the doc string (the triple quotes) will be read as SQL syntax. Because of this, if some person wanted to submit a username as `DROP TABLES` which is a SQL statement for destroying your tables, it will run.
* With the question marks we ensure that every value being passed into our query is not read as a SQL statement but just as a string being passed in. 

#### Part 4 - Models

* Alright our database has been made and we have some data in there to mess around with.
* Now it's time to get to the M in MVC
* Remember the point of the `Models` is to communicate with our database.
* Below is an example of how we can use the sqlite3 library to run SQL queries inside a py file.

```
import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";
conn.close()
```
* Great it looks similar to what we did earlier. 
* There is no `.commit()` method being run
* This is because we only use `.commit()` when we are manipulating the database
* In the example above we are only using SELECT (or READ in CRUD) and grabbing data. 
* This looks great but how can we actually write our code to run queries only at certain points, and also return what was found. 
* Same way we've been writing the Views and the Controllers

```
import sqlite3

class Classname:

	def __init__(self, x, y, z):
		blah blah blah
	
	def create_login(self,username, password):
		conn = sqlite3.connect('databasename.db')
		c = conn.cursor()
		
		the_variable = c.execute(
			"""
			SQL COMMAND HERE. (INSERT INTO tablename blah blah)
			"""
		)
		
		return the_variable.fetchall()
```

#### Resources

* [SQLite3 Python Tutorials Point](http://www.tutorialspoint.com/sqlite/sqlite_python.htm)
* Use dir() to look at the various methods that the sqlite3 module gives you
* [The Python3 SQLite docs](https://docs.python.org/3.4/library/sqlite3.html)