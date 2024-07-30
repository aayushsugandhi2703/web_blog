from secret import get_secret_key
class Config:
    SECRET_KEY = get_secret_key()
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tasks_db.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False