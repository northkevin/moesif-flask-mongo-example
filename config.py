"""This module is to configure app to connect with database."""
import os

from pymongo import MongoClient

db_name = os.environ.get('MONGODB_NAME')
port = int(os.environ.get('MONGODB_PORT'))

DATABASE = MongoClient()['onedrive-data'] # DB_NAME
DEBUG = True
client = MongoClient('localhost', port)
