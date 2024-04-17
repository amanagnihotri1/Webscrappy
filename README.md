[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# **Webscrappy**
This is a simple web scraper project built with Python using BeautifulSoup for web scraping, Requests for making HTTP requests, PostgreSQL for database storage, and CSV for data export contains simple functions to execute one afte the ohter to first fetch data and then create CSV file by fetching data from Postgres Table.



## Features
- **Web Scraping**: Utilizes BeautifulSoup for parsing HTML and extracting data from websites.
- **HTTP Requests**: Uses the Requests library to fetch web pages.
- **Data Storage**: Stores scraped data into a PostgreSQL database.
- **Data Export**: Provides functionality to export scraped data to CSV format.
## Prerequisites

Before running this project, ensure you have the following installed:

- ### Python 
    Initial Setup is required to run all Python files.You can download Python from Here-https://www.python.org/downloads/ and setup on your system.
  
- ### BeautifulSoup 
    Beautiful Soup is a library that makes it easy to scrape       information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree. 
- ### Requests 
    Requests is an HTTP client library for the Python programming  language.You can read documentation here
- ### psycopg2  
    Psycopg is PostgreSQL database adapter for Python. It's main features are the complete implementation of the Python DB API 2.0 specification and the thread safety
- ### PostgreSQL 
    PostgreSQL is a powerful, open source object-relational database system with over 35 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.
## Steps to run Locally

1. Install all the prerequisites first

2. Go to the project directory

```bash
  cd your_project_folder_name
```
3. Clone the project
```bash
  git clone https://github.com/amanagnihotri1/Webscrappy
```

4. Install required packages to achieve scrapping

```bash
  pip install beautifulsoup4 pyscopg2 requests
```
**Setup Postgresql credentials**

```bash
dbname="your_db_name",
user="your_user_name",
password="your_password",
host="your_hostname",
port="your_portname",
```
Run this command to initiate crwaling and to create table

```bash
python main.py
```
Run this command to generate CSV file for data present in Table

```bash
python csv_generator.py

```

3. A CSV file will appear in working directory with name **output.csv**

## Screenshots
 #### Generated CSV file
![screenzy-1713336091558](https://github.com/amanagnihotri1/Webscrappy/assets/69078309/2d66a8ef-4bed-459a-b52b-e51e582ac91b)


## Authors

- [@amanagnihotri1](https://www.github.com/amanagnihotri1)

