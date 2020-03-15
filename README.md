# Task2 Excel to Database

This is the project to demonstrate the ETL pipeline and how to import the Excel file to the MySQL database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and the Python libraries.

The Python libraries listed in requirements.txt
```
pandas==0.25.3
xlrd==1.2.0
python-dotenv==0.12.0
PyMySQL==0.9.3
requests==2.23.0
```

### Installing

How to install them step by step.

```
sudo apt-get update
sudo apt-get install mysql-server

sudo apt install python3-pip
pip3 install -r requirements.txt
```

Then run the database script (db_script.sql) to create the user, the database, and the database table.

## Running the pipeline

```
python3 main.py
```