import os
from datetime import timedelta

class Config:
  

    Upload_Folder = os.path.join(os.getcwd(), '..', 'static')
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.urandom(24)
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=1000000)

    # Redis Config
    CACHE_TYPE= 'RedisCache'
    CACHE_REDIS_URL= 'redis://localhost:6379/3'
    CACHE_DEFAULT_TIMEOUT= 300
     

    