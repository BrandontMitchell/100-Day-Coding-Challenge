# Day 048 - Introduction to SQL

The purpose of this day is to get a brief introduction to SQL. SQL is a programming language written to work with **relational databases**. Think of them as really large excel spreadsheets where the rows correspond to a single entry, and each column provides an extra piece of information about that table entry.

Databases give us a great improvement in the way that we can process and retrieve large datasets. They are fast, gigantic, and secure. Most relevantly, they offer many programmatic capabilities in terms of searching and updating the information stored in them. That's where SQL comes in. **Structured Query Language** (SQL) is a standard syntax that is used by all database software. It's what we'll be gaining experience with for today's challenge.

## Starter Code

This day includes a single file in the starter-code folder titled `starter.sql`. However, this file doesn't contain any actual starter-code. In fact, you won't be creating a file for today's challenge. SQL is difficult to test/work with if you don't have a database set up beforehand that you can interact with. So we'll be using an interface courtesy of my web programming class.

You can also find it [here](https://webster.cs.washington.edu/cse154/query/). Once you navigate to the website, select the `world` database. You can ignore the login in the upper-right part of the web page.

You will be writing a SQL query to...

1. List all of the official languages spoken around the world in reverse alphabetical order.

2. List all countries that have the word Republic as part of their name.

3. List the names of all countries that are not in Africa.

4. List the name and gnp of countries that have a GNP between $10,000 AND $50,000.

5. (Extra-Credit) List the name, population, surface_area, and population_density of all countries, ordered by population densities (descending).
  
## Getting Started
  
SQL is a **declarative** language. This means that you will be describing what data you are seeking, not exactly how to find it. It's a pretty intuitive language that reads really nicely, almost like English. We'll start off with the `SELECT` statement.

### Syntax
```
SELECT column(s) FROM table;
```

### Example
```
SELECT name, release_year FROM Games;
```

The `SELECT` statement is used to select and return data from a database. Table and column names are case-sensitive. SQL statements are written in all uppercase by convention, although this is not strictly necessary. It will be used in examples so you can more easily distinguish between statements and column/table names.

The `DISTINCT` modifier eliminates duplicates from the result.

### Syntax
```
SELECT DISTINCT column(s) FROM table;
```

### Example
```
SELECT DISTINCT release_year
FROM Games;
```

Notice that you also have a lot of freedom on where to include whitespace and where not to. The important thing is that you include a semicolon at the end of your query. **Query** is the word that we'll be using to describe a SQL statement.

Next, we'll talk about the `WHERE` statement.

### Syntax
```
SELECT column(s) FROM table WHERE condition(s);
```

### Example
```
SELECT name, release_year FROM Games WHERE genre = 'puzzle';
```

The `WHERE` clause filters out rows based on their columns' values. The `WHERE` clause can also be used in combination with logical and relational operators:

### Example 1
```
SELECT name, release_year
FROM Games
WHERE release_year < 1990;
```
### Example 2
```
SELECT name, release_year FROM Games
WHERE release_year BETWEEN 1990 AND 2000;
```

Multiple `WHERE` conditions can be combined using `AND`, `OR`, and `BETWEEN`. You can also use `LIKE` to approximate matches.

### Syntax
```
WHERE column LIKE pattern
```

### Example
```
SELECT name, release_year FROM Games
WHERE name LIKE 'Spyro%'
```

Here's how you write the pattern part:

* `LIKE 'text%'`
  * searches for text that starts with a given prefix
* `LIKE '%text'`
  * searches for text that ends with a given suffix
* `LIKE '%text%'`
  * searches for text that contains a given substring
  
You can use the `ORDER BY` keyword to sort the result set in ascending or descending order.

### Syntax
```
SELECT column(s) FROM table
ORDER BY column(s) ASC|DESC;
```

### Example
```
SELECT name FROM Games
ORDER BY name DESC
```

`ASC` corresponds to alphabetical order, and `DESC` corresponds to reverse-alphabetical order.

SQL, similar to HTML, works best by experimenting rather than being told what to do. Start off by experimenting with the SQL tester website, and then see if you can complete the 5 challenge queries.
