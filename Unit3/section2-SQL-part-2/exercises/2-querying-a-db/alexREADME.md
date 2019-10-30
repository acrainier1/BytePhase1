## Querying a SQL Database

In this challenge you are given a SQL database with data inside. You will need to mine it for important information.

Open it up in terminal by typing
```bash
$ sqlite3 sitemetrics.db
```
To see the existing tables and columns, use the .schema command. Map this by hand or on SQL designer so you have a greater understanding of what we're working with.

#### Answer the following questions in this file, with the results and the sql you wrote to get it.
-------------

##### How many people are from California? 
  - 14

  SELECT COUNT(*) FROM users WHERE state="CA";


##### Who has the most page views? How many do they have, and where are they from?
 - 179|Edison Mcintyre|hattie.harriet@far.me|Mauriceville|ME|2014-06-02|19937

  SELECT * FROM users ORDER BY page_views ASC;


##### Who has the least page views? How many do they have and where are they from?
 - 477|Hattie Ross|jeffery.travis.jeff@laugh.info|Hubbard|MA|2014-07-19|16

 SELECT * FROM users ORDER BY page_views DESC;


##### Who are the most recent visitors to the site?(at least 3)
 - Otha Ortiz
 - Selina Hardy
 - Terrance Allen

SELECT name FROM users ORDER BY last_visit ASC;


##### Who was the first visitor?
- Woodrow Duffy

 SELECT name FROM users ORDER BY last_vist DESC;


##### Who has an email address with the domain 'horse.edu'?
 - Fern Byers|lino.jarod@hornhorse.edu
 - Valentine Gonzales|steve.louis.jeremy@horse.edu

 SELECT name, email FROM users WHERE email LIKE "%horse.edu";


##### How many people are from the city Graford?
 - 3

 SELECT COUNT(*) FROM users WHERE city="Graford";


##### What are the names of all the cities that start with the letter V, in alphabetical order?
 - Valley View
 - Van
 - Vega
 - Victoria

 SELECT city FROM users WHERE city LIKE "V%" GROUP BY city;


##### What are the names and home cities for people who searched for the word "drain"?

 - Nelly Beach|Graford
 - Penelope Stein|Runaway Bay
 - Tisha Gill|Bausell and Ellis
 - Rolando Crowley|Buda

 SELECT users.name, users.city
    FROM users 
    JOIN user_searches 
    JOIN search_terms 
    ON users.id=user_searches.user_id 
    AND user_searches.term_id=search_terms.id 
    WHERE search_terms.word="drain";

##### How many times was "trousers" a search term?
 - 2

 SELECT COUNT(*)
    FROM user_searches
    JOIN search_terms
    ON user_searches.term_id=search_terms.id
    WHERE search_terms.word="trousers";


##### What were the search terms used by visitors who last visited on August 22 2014?
 - very long list

 SELECT search_terms.word
    FROM search_terms 
    JOIN user_searches
    JOIN users 
    ON user_searches.user_id=users.id 
    WHERE users.last_visit="2014-08-22"
    GROUP BY search_terms.word;


##### What was the most frequently used search term by people from Idaho?
 - ? Idaho doesn't work so I did Iowa (IA) instead
 - from sqlite3 in bash: Error: ambiguous column name: ID
 - "with" is most commonly searched term for Iowans.

 SELECT word, COUNT(*)
    FROM search_terms
    JOIN user_searches
    JOIN users
    ON search_terms.id=user_searches.term_id
    AND user_searches.user_id=users.id
    WHERE users.state="GA"
    GROUP BY search_terms.word
    ORDER BY COUNT(*) ASC;

##### What is the name of user 391, and what are his search terms?
 - Stan Alston|ornament
 - Stan Alston|heat
 - Stan Alston|sex
 - Stan Alston|secret
 - Stan Alston|dry

 SELECT name, word 
    FROM search_terms 
    JOIN user_searches 
    JOIN users 
    ON search_terms.id=user_searches.term_id 
    AND user_searches.user_id=users.id 
    WHERE users.id=391;

