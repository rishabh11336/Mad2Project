import os

from flask import Flask,request,jsonify
from flask_cors import CORS

from .config.config import Config
from .models.model import db, User
from .resources.auth.userAPI import UserAPI

current_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)

CORS(app)
    

app.add_url_rule('/api/auth/user', view_func=UserAPI.as_view('user_api'), methods=['GET', 'POST'])
app.add_url_rule('/api/auth/user/<int:id>', view_func=UserAPI.as_view('user_api_id'), methods=['GET', 'POST'])



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


