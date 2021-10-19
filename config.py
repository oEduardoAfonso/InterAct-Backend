import os

DEBUG = True
USERNAME = 'postgres'
PASSWORD = 'postgres'
SERVER = 'localhost'
DB = 'InterAct'
DATABASE_URL = f'postgresql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'

def url():
    if os.getenv('DATABASE_URL', DATABASE_URL) != DATABASE_URL:
        return os.getenv('DATABASE_URL').replace("://", "ql://", 1)
    else:
        return DATABASE_URL

SQLALCHEMY_DATABASE_URI = url()
SQLALCHEMY_TRACK_MODIFICATIONS = True

