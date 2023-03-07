"""Created the file to handle the db connection"""
import os

import MySQLdb
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

connection = MySQLdb.connect(
    host=os.environ.get("MYSQL_HOST"),
    port=os.environ.get("MYSQL_PORT"),
    user=os.environ.get("MYSQL_USER"),
    password=os.environ.get("MYSQL_PASSWORD"),
    db=os.environ.get("MYSQL_DB"),
)
