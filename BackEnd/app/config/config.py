import os

class Config:
    Upload_Folder = os.path.join(os.getcwd(), '..', 'static')
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False