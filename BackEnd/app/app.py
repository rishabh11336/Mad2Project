import os

from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from .config.config import Config
from .models.model import db, bcrypt, User
from .resources.auth.userAPI import UserAPI, RegisterAPI, LoginAPI, LogoutAPI

current_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
bcrypt.init_app(app)
jwt = JWTManager(app)
CORS(app)
CORS(
    app,
    resources={
        r"/*": {
            "origins": "http://localhost:5173",
            "supports_credentials": True,
            "Access-Control-Allow-Credentials": True,
        }
    },
)

app.add_url_rule('/api/auth/user', view_func=UserAPI.as_view('user_api'), methods=['GET'])
app.add_url_rule('/api/auth/register', view_func=RegisterAPI.as_view('register_api'), methods=['POST'])
app.add_url_rule('/api/auth/login', view_func=LoginAPI.as_view('login_api'), methods=['POST'])
app.add_url_rule('/api/auth/logout', view_func=LogoutAPI.as_view('logout_api'), methods=['POST'])


with app.app_context():
    db.create_all()
    user = User.query.filter_by(username='admin').first()
    
    if not user:
        user = User(
            username='admin',
            password=bcrypt.generate_password_hash('12345').decode('utf-8'),
            role='admin',
            email='admin@mail.com',
            approved=True)
        db.session.add(user)
        db.session.commit()


