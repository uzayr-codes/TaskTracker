# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Add more settings as needed, for example:
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
