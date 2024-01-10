import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config.config import Config

current_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

app.config.from_object(Config)

@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)