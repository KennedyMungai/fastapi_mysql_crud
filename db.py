"""Created the file to handle the db connection"""
import os

import pymysql
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

connection = pymysql.connect(
    host=os.environ.get("MYSQL_HOST"),
    port=os.environ.get("MYSQL_PORT"),
    user=os.environ.get("MYSQL_USER"),
    password=os.environ.get("MYSQL_PASSWORD"),
    db=os.environ.get("MYSQL_DB"),
)

cursor = connection.cursor()
