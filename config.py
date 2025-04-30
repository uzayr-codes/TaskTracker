# config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Use SQLite as an example
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Optional: Disable Flask-SQLAlchemy modification tracking
    SECRET_KEY = "36229e7f-c386-4893-b428-c944ef3dd929"  # You should change this to a strong secret key for session security
