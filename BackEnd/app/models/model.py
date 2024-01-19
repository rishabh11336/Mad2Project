from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
    role = db.Column(db.String(32), nullable=False, default='user')
    approved = db.Column(db.Boolean, default=True)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "approved": self.approved,
        }
class TokenBlacklist(db.Model):
    __tablename__ = 'token_blacklist'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(250), unique=True, nullable=False)
    
    
    def serialize(self):
        return {
            "id": self.id,
            "token": self.token
        }
    
class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    description = db.Column(db.String(128), nullable=False)
    image = db.Column(db.String(128), nullable=False)
    createdBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    dateCreated = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    Products = db.relationship('Product', backref='category', lazy=True)
    approved = db.Column(db.Boolean, default=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "image": self.image,
            "createdBy": self.createdBy,
            "dateCreated": self.dateCreated,
            "approved": self.approved,
        }
    
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    image = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    si_unit = db.Column(db.String(32), nullable=False)
    best_before = db.Column(db.DateTime, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    createdBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    dateCreated = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    approved = db.Column(db.Boolean, default=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "price": self.price,
            "quantity": self.quantity,
            "si_unit": self.si_unit,
            "best_before": self.best_before,
            "category_id": self.category_id,
            "createdBy": self.createdBy,
            "dateCreated": self.dateCreated,
            "approved": self.approved,
        }

class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product_name = db.Column(db.String(32), db.ForeignKey('product.name'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, db.ForeignKey('product.price'), nullable=False)
    dateCreated = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "product_id": self.product_id,
            "product_name": self.product_name,
            "quantity": self.quantity,
            "price": self.price,
            "dateCreated": self.dateCreated,
        }