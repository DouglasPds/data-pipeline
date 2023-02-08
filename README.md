# data-pipeline

Environment chose:
1. Language Python.
2. File format csv.
3. Database MySql.

Requirements for python:
1. pandas
2. sqlalchemy
3. psycopg2
4. pymysql

## Instructions to run the pipeline

* Run `docker compose up -d`
  - To run the container of postgres, create the database and insert the tables and their values
* Run `python extract.py`
  - To read the source data and generate the files
* Run `docker compose -f docker-compose.load.yml up -d`
  - To run the container of mysql and create the database
* Run `python load.py`
  - To load the files into tables in the mysql database
* Now we can perform the sql query to get the orders and their details, like the one inside sqlFinalStep folder, 
or other more specifically showing only some columns, filtering by data, or limiting the showed rows for performance purposes.
