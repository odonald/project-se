from dotenv import load_dotenv
from os import environ

load_dotenv()

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL').replace('postgres://', 'postgresql://', 1)
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = '74081e0e33c1046bd8f96bb3528e857c21b1064ad6f47f8f'



