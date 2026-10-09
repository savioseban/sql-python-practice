# SQL + Python Practice

Small practice project that connects Python to a MySQL database, reads data from it, and exports the result to CSV for use in BI tools.

## What it does

- `test.py` connects to a local MySQL database and prints the rows of a `students` table.
- `export.py` reads the same table with pandas and saves it as `students.csv`.

## Tools used

- Python 3.12
- MySQL Server 8.0 and MySQL Workbench
- pandas
- mysql-connector-python

## Setup

1. Install the libraries:

2. Create the practice database in MySQL:
   ```sql
   CREATE DATABASE practice;
   USE practice;

   CREATE TABLE students (
     id INT PRIMARY KEY AUTO_INCREMENT,
     name VARCHAR(50),
     city VARCHAR(50)
   );

   INSERT INTO students (name, city)
   VALUES ('Savio', 'Trivandrum'), ('Anu', 'Kochi');
    ```
3. Open `test.py` and `export.py` and replace `YOUR_PASSWORD` with your own MySQL root password.

## Run

## What's next

- Load the exported CSV into Tableau Public
- Connect Power BI directly to the MySQL database
- Build a larger project with a real dataset and a dashboard
