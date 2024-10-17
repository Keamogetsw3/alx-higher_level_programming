# 0x0D. SQL - Introduction
## Project Overview


![image](https://github.com/user-attachments/assets/145c4308-a8bf-4e5c-acc5-b9294767c1c5)
![image](https://github.com/user-attachments/assets/4b368271-b3af-4fcd-b51b-863f7ce613f2)

This project introduces SQL and MySQL, focusing on fundamental concepts and commands used in relational databases.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Concepts](#concepts)
3. [Resources](#resources)
4. [Learning Objectives](#learning-objectives)
   - [Databases](#databases)
   - [Relational database](#relational-database)
   - [SQL](#sql)
   - [MySQL](#mysql)
      - [How to create a database in MySQL](#how-to-create-a-database-in-mysql)
   - [The meanings of DDL and DML](#the-meanings-of-ddl-and-dml)
   - [How to CREATE or ALTER a table](#how-to-create-or-alter-a-table)
   - [How to SELECT data from a table](#how-to-select-data-from-a-table)
   - [How to INSERT, UPDATE, or DELETE data](#how-to-insert-update-or-delete-data)
   - [What subqueries are and how to use them](#what-subqueries-are-and-how-to-use-them)
   - [How to use MySQL functions](#how-to-use-mysql-functions)
5. [Requirements](#requirements)


## Concepts

For this project, familiarize yourself with the following concepts:

- **Databases**: Understanding what a database is and its types.
- **Relational Databases**: Key principles and differences.
- **SQL**: Basics of SQL, including data definition and manipulation.
- **MySQL**: Overview and basics of using MySQL.

## Resources

To complete this project, refer to the following resources:

- [What is Database & SQL?](#)
- [A Basic MySQL Tutorial](#)
- [Basic SQL Statements: DDL and DML](#) (Skip "Privileges" chapter)
- [Basic Queries: SQL and RA](#)
- [SQL Technique: Functions](#)
- [SQL Technique: Subqueries](#)
- [Difference Between Backtick and Apostrophe](#)
- [MySQL Cheat Sheet](#)
- [MySQL 8.0 SQL Statement Syntax](#)
- [Installing MySQL in Ubuntu 20.04](#)

## Learning Objectives

By the end of this project, you should be able to explain:

### Databases

- **What a database is**  
  - A database is a system used to store data in a way that it remains available and organized even when the application or server is not running. Unlike storing data in the application's memory, which is temporary and lost when the server stops, databases ensure the data is stored permanently.

- **Why not just store data in flat files?**  
  - Flat files (like text or JSON files) can store data, but databases are much more reliable and efficient because they follow ACID principles:  
    - **Atomicity**: A transaction is either fully completed or not at all. If part of a process fails, nothing is saved.  
    - **Consistency**: Data must follow defined rules, and any transaction violating those rules is rejected.  
    - **Isolation**: Multiple operations happening at the same time don’t interfere with each other.  
    - **Durability**: Once a transaction is completed, data will survive any crash or server failure.  

  - Besides, databases are designed for strong performance and can handle large amounts of data efficiently, unlike flat files.

- **CRUD Operations**  
  - The four basic operations performed on a database are known as **CRUD**:  
    - **Create**: Add new data.  
    - **Read**: Retrieve existing data.  
    - **Update**: Modify data.  
    - **Delete**: Remove data.  

- **Types of Databases**  
  - **Relational Databases (SQL)**:  
    - These store data in tables with rows and columns. Common examples include PostgreSQL, MySQL, and Oracle.  
    - They use **SQL (Structured Query Language)** to perform CRUD operations.  
    - Relational databases use relations (or links) between different tables. For example, in a blog, a comment can be related to a specific post by storing the post’s ID in the comment record.  

  - **NoSQL Databases**:  
    - Non-relational databases that are more flexible with how they store data. They are often used for large-scale applications or where flexibility is needed.  
    - Popular NoSQL databases include MongoDB (document-based) and Redis (key-value store).  
    - NoSQL databases don’t always require fixed schemas and can store data in formats like JSON.  

- **SQL vs NoSQL**  
  - **SQL**: Uses structured tables and SQL queries, offering high consistency, reliability, and efficiency for large-scale data transactions.  
  - **NoSQL**: More flexible, schema-less databases. They are easier to start with and are used for big data applications, but they are sometimes harder to scale and may require additional work to ensure data structure.  

- **Terminology in Relational Databases**  
  - **Tables**: Where data is stored.  
  - **Columns**: Attributes of the data (like `id`, `name`).  
  - **Rows**: Individual records in the table.  
  - **Primary Key**: A unique identifier for a row.  
  - **Foreign Key**: A column that links to another table’s primary key, establishing a relationship between two tables.  

- **Advanced Features**  
  - **Indexes**: Speed up data retrieval by precomputing certain queries, making the database perform faster on common tasks.  
  - **Joins**: Combine data from multiple tables based on relationships (like fetching all comments related to a post).  

- **NoSQL Examples**  
  - **Document-based Databases**: Like MongoDB, which stores data as flexible documents (often in JSON format).  
  - **Key-Value Stores**: Like Redis, which stores data as key-value pairs, useful for fast retrieval of simple data.  

### Relational databases
- What a relational database is.
   - A relational database (RDB) is a way of structuring information in tables, rows, and columns.
   - An RDB has the ability to establish links—or relationships–between information by joining tables
   - which makes it easy to understand and gain insights about the relationship between various data points.
   - A **relational database management system (RDBMS)** is a program used to create, update, and manage relational databases.
   - Some of the most well-known RDBMSs include **MySQL, PostgreSQL, MariaDB, Microsoft SQL Server, and Oracle Database**.

### SQL
- What SQL stands for.
   - Invented by Don Chamberlin and Ray Boyce at IBM, Structured Query Language (SQL) is the standard programming language for interacting with relational database management systems,
   -  allowing database administrator to add, update, or delete rows of data easily.
   -  Originally known as SEQUEL, it was simplified to SQL due to a trademark issue.
   -  SQL queries also allows users to retrieve data from databases using only a few lines of code.
   -  Given this relationship, it’s easy to see why relational databases are also referred to as “SQL databases” at times. 

### MySQL
- ### What MySQL is.
   - MySQL is an open source relational database management system (RDBMS) that's used to store and manage data
- ### How to create a database in MySQL.
  ``` python
  CREATE DATABASE my_database; #The CREATE DATABASE statement is used to create a new SQL database.
  SHOW DATABASES; #check if the database was created successfully


- The meanings of DDL and DML.
- Some of The Most Important SQL Commands
   - SELECT - extracts data from a database
   - UPDATE - updates data in a database
   - DELETE - deletes data from a database
   - INSERT INTO - inserts new data into a database
   - CREATE DATABASE - creates a new database
   - ALTER DATABASE - modifies a database
   - CREATE TABLE - creates a new table
   - ALTER TABLE - modifies a table
   - DROP TABLE - deletes a table
   - CREATE INDEX - creates an index (search key)
   - DROP INDEX - deletes an index

- How to CREATE or ALTER a table.
- How to SELECT data from a table.
- How to INSERT, UPDATE, or DELETE data.
- What subqueries are and how to use them.
- How to use MySQL functions.

## Requirements

### General

- **Allowed Editors**: vi, vim, emacs
- **Execution Environment**: Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- **File Requirements**:
  - Files must end with a new line.
  - SQL queries must include a comment describing the task just before the query.
  - All SQL keywords must be in uppercase (e.g., SELECT, WHERE).
  - Files should start with a comment describing the task.
  - A `README.md` file is mandatory at the root of the project folder.
- **File Length**: The length of your files will be tested using `wc`.
