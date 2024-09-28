# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/inventory_db'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/inventory_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False