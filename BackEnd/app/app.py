import os

from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from .config.config import Config
from .models.model import db, bcrypt, User, Product, Category
from .resources.auth.userAPI import UserAPI, RegisterAPI, LoginAPI, LogoutAPI
from .resources.Products.productAPI import ProductAPI 
from .resources.Products.categoryAPI import CategoryAPI
from .resources.operations.cartAPI import CartAPI
from .resources.operations.orderAPI import OrderAPI

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

# Authentication
app.add_url_rule('/api/auth/user', view_func=UserAPI.as_view('user_api'), methods=['GET'])
app.add_url_rule('/api/auth/register', view_func=RegisterAPI.as_view('register_api'), methods=['POST'])
app.add_url_rule('/api/auth/login', view_func=LoginAPI.as_view('login_api'), methods=['POST'])
app.add_url_rule('/api/auth/logout', view_func=LogoutAPI.as_view('logout_api'), methods=['POST'])

# Products
app.add_url_rule('/api/products', view_func=ProductAPI.as_view('product_api'), methods=['GET', 'POST'])
app.add_url_rule('/api/products/<int:id>', view_func=ProductAPI.as_view('product_api_id'), methods=['GET', 'PUT', 'DELETE'])

# Categories
app.add_url_rule('/api/categories', view_func=CategoryAPI.as_view('category_api'), methods=['GET', 'POST'])
app.add_url_rule('/api/categories/<int:id>', view_func=CategoryAPI.as_view('category_api_id'), methods=['GET', 'PUT', 'DELETE'])

# Cart
app.add_url_rule('/api/cart', view_func=CartAPI.as_view('cart_api'), methods=['GET', 'POST'])
app.add_url_rule('/api/cart/<int:id>', view_func=CartAPI.as_view('cart_api_id'), methods=['DELETE'])

# Order
app.add_url_rule('/api/order', view_func=OrderAPI.as_view('order_api'), methods=['POST'])

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


