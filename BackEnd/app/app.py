import os

from flask import Flask,request,jsonify
from flask_cors import CORS

from .config.config import Config
from .models.model import db, User
current_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)

@app.route('/', methods=['POST'])
def hello_world():
    data = request.get_json()
    username = data['username']
    password = data['password']
    checkuser = User.query.filter_by(username=username, password=password).first()
    if checkuser:
        return jsonify({'auth' : 'success'})
    else:
        return jsonify({'auth' : 'Invalid username or password'})
    

with app.app_context():
    db.create_all()
    user = User.query.filter_by(username='admin', password='12345').first()
    
    if not user:
        user = User(
            username='admin',
            password='12345',
            role='admin',
            email='admin@mail.com',
            approved=True)
        db.session.add(user)
        db.session.commit()


