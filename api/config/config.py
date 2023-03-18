import os
from decouple import config
from datetime import timedelta
import re

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

db_name = 'studentapi_db'

default_uri = "postgres://{}:{}@{}/{}".format('postgres', 'password', 'localhost:5432', db_name)

uri = os.getenv('DATABASE_URL', default_uri) # or other relevant config var
if uri.startswith('postgres://'):
    uri = uri.replace('postgres://', 'postgresql://', 1)

# DATABASE_URL = os.environ.get('postgres://hywjcndkxckgre:1b1dc1a76e4fb939e3c605ff985114fd3bb4f3d404832bf9bcd72eaaaeb1904f@ec2-52-205-45-222.compute-1.amazonaws.com:5432/dfjvm6n0apg6oc')


class Config:
    SECRET_KEY = config('SECRET_KEY', 'secret')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR, 'db.sqlite3')
    
    
class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = config('DEBUG', False, cast=bool)
    
config_dict = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}        