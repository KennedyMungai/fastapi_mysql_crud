"""Created the file to handle the db connection"""
import os

import pymysql
from pymysql import Error
from dotenv import find_dotenv, load_dotenv

from sqlalchemy import MetaData


meta = MetaData()


load_dotenv(find_dotenv())

connection = pymysql.connect(
    host=os.environ.get("MYSQL_HOST"),
    port=int(os.environ.get("MYSQL_PORT")),
    user=os.environ.get("MYSQL_USER"),
    password=os.environ.get("MYSQL_PASSWORD"),
    db=os.environ.get("MYSQL_DB"),
)

try:
    cursor = connection.cursor()
    cursor.execute('select database();')
    db = cursor.fetchone()
    print("You are connected to the database: ", db)
except Error:
    print("Error occurred while connecting to MySQL db", Error)
finally:
    cursor.close()
    connection.close()
    print("MySQL connection is closed")
