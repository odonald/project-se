from dotenv import load_dotenv
from os import environ

load_dotenv()

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = environ.get('SECRET_KEY')



