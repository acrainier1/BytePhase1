# Relational Databases / SQLite 3

### Learning Objectives
***Students Will Be Able To...***

* Diagram the ERD's of a relational database
* Start a sqlite3 database
* Access sqlite3 database
* Execute CRUD commands utilizing SQL queries

---

### Context

* Databases are used to store large amounts of data. 
* SQL is a database language which allows us to interact with databases. 

---

#### What is SQL? What is CRUD?

* So we've talked about databases, and we've drawn them out. 
* Time to make a database and talk to it
* To build our database we will be using SQLite3

***SQL***

* SQL - Structured Query Language
* It's main and only purpose is the management of relational databases
* Below are two terms that is not necessary to help you in programming but is fun to know a little about. 
	* DSL - What is a DSL? DSL stands for Domain Specific Language
	* GPL - What is a GPL? GPL stands for General Purpose Language

***CRUD***

* CRUD is a programming concept used to express the four main responsibilities of HTTP Methods
* CRUD stands for Create, Read, Update, and Delete
* Notice that these 4 concepts encapsulates everything we do with the internet. 
	* When we make new accounts on websites
	* Update our existing accounts
	* Delete accounts
	* Search accounts

| Operation | HTTP       | SQL          |
|-----------|------------|--------------|
| Create    | PUT / POST | INSERT INTO  |
| Read      | GET        | SELECT       |
| Update    | PUT        | UPDATE       |
| Delete    | Delete     | Delete       |


#### Part 4 - Let's Begin CRUDDING!!! (Create and Read)

* Lets make a new folder outside of your byte academy folder
	* You can copy and paste the class example into the daily repo later if you want a reference. However everything in that example will be in this lesson plan. 
* Now lets `cd` into that folder and make a new database
* The syntax to create a database in SQLite3 is just `sqlite3 database_name`

```
sqlite3 Ferrall.db
```
* We now have a database file in your directory. 
* Your terminal should have you already in the sqlite database
* This database is currently empty
* Remember that a database can have multiple tables
* For the purposes of this lesson we will just make one table to practice our CRUD operations on

```
CREATE TABLE william (id INTEGER PRIMARY KEY, character TEXT, movie TEXT, year INTEGER);
```
* The semi colon at the end is a necessity. It tells sql that you are done with that command. 
* Commands in SQL should be written in all CAPS. This is to distinguish them from your databases names and columns. In some SQL languages this is enforced. In SQLite3 it's the wild west. 
* `william` is the name of the table we just created
* `id` / `character` / `movie` are the names of the column
* They are defined by capitalized `INTEGER`, `TEXT`, and `INTEGER`
* `PRIMARY KEY` is put on the `id` column to tell SQL that this is a unique column. There will not be any rows with the same id number
* SQLite will insert the id into the rows automatically
* Let's take a look at our schema. The schema will return to us the format of the table that we just made using the `CREATE` statement. 

```
.schema william
```
* How do we insert information into our table? 
* Here we are following the `C` in CRUD.

```
INSERT INTO william (character, movie, year) VALUES ("Ron Burgundy", "Anchorman 2", 2013);
```
* Now lets look at our table and see if it went in

```
SELECT * FROM william;
```
* You just did the `R` in CRUD with the `SELECT` statement
* The `splat` in the above command tells us to grab everything from the table william
* Okay so now it's your turn to add more items to the databse

***Five Min Exercise***

* Fill out your william table with the below values exactly as is
* Yes I know some of these are incorrect or have typos or are the same. We're going to be fixing them later on

| Character              | Movie            | Year |
|------------------------|------------------|------|
| Ron Burgundy           | Anchorman 2      | 2013 |
| Cam Brady              | The Campaign     | 2012 |
| Mugatu                 | Zoolander 2      | 2001 |
| Armando                | Casa de mi Padre | 2012 |
| Allen Gamble           | The Other Guys   | 2010 |
| Allen Gamble           | Semi-Pro         | 2008 |
| Mugatu                 | Zoolander        | 2001 |
| Chazz Michael Michaels | The Campaign     | 2007 |

* Run SELECT * FROM to see all the movies in the william table

---

* How can we select only one value from the table?
* How can we select values that have the same attribute?

```
SELECT * FROM william WHERE year = 2012;
SELECT * FROM william WHERE character = "Allen Gamble";
```
* The `WHERE` statement allows us to add conditionals to our queries. We will be using `WHERE` in areas other than `READ/SELECT`
* Alright so we got the `CR` in CRUD
* Now lets work on the `UD`
* Notice we have two Allen Gamble's
* Let's change the one that belongs to the movie "semi-pro" to the actual character name "Jackie Moon"

```
UPDATE william SET character = "Jackie Moon" WHERE movie = "Semi-Pro";
```
* Be careful with not using a unique identifier for the WHERE statement. You will be editing all of the values that pass the conditions parameter
* For example lets run another update

```
UPDATE william SET character = "The Real Slim Shady" WHERE movie = "The Campaign";
```
* Notice how both rows with the campaign has the character updated to the real slim shady
* Alright lets fix those two movies and move on. If you need to find the specific row we can use the select statement again

```
SELECT * FROM william;

UPDATE william SET character="Cam Brady" WHERE id = 2;

UPDATE william SET character = "Chazz Michael Michaels" WHERE id = 9;

Update william SET movie = "Blades of Glory" WHERE id = 9;
```
* Alright enought practice with Update
* Let's cover Delete

```
DELETE FROM william WHERE year = 2013

DELETE FROM william WHERE character = "Mugatu"
```

#### Part 4 - Resources

- [SQLite3 datatype reference](https://www.sqlite.org/datatype3.html)
- [SQL Visualizer](http://ondras.zarovi.cz/sql/demo/)
- [Beginner SQL Tutorial](http://beginner-sql-tutorial.com/sql-query-tuning.htm)
- [SQL Course](http://www.sqlcourse.com/)

