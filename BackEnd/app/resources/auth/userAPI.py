from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    get_jwt,
    jwt_required,
)
from flask_jwt_extended.exceptions import JWTDecodeError
from app.models.model import User, TokenBlacklist, db, bcrypt

def custom_jwt_required():
    def decorator(fn):
        @jwt_required()
        def wrapper(*args, **kwargs):
            try:
                jti = get_jwt()["jti"]
                token_in_blacklist = TokenBlacklist.query.filter_by(token=jti).first()
                if token_in_blacklist:
                    return jsonify({"message": "Token has been revoked"}), 401
                return fn(*args, **kwargs)
            except JWTDecodeError:
                return jsonify({"message": "Invalid token"}), 401

        return wrapper

    return decorator

class UserAPI(Resource):
    @custom_jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = User.query.filter_by(username=current_user['username']).first()
        if not user:
            return jsonify({"msg": "User not found"}), 404
        return jsonify(user.serialize())

class RegisterAPI(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user:
            return jsonify({"msg": "User already exists"}), 400
        user = User(
            username=data['username'],
            password=bcrypt.generate_password_hash(data['password']).decode('utf-8'),
            role='user',
            email=data['email'],
            approved=True)
        db.session.add(user)
        db.session.commit()
        return jsonify(user.serialize() | {'message':'user registered'}), 201
    
class LoginAPI(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if not user:
            return jsonify({"msg": "User not found"}), 404
        if not bcrypt.check_password_hash(user.password, data['password']):
            return jsonify({"msg": "Password is incorrect"}), 401
        if not user.approved:
            return jsonify({"msg": "User not approved"}), 401
        access_token = create_access_token(
            identity={"username": user.username, "email": user.email, "role": user.role}
        )
        return jsonify({'access_token' : access_token, "message":f"Welcome {user.username}!"}), 200    
    
class LogoutAPI(Resource):
    @custom_jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        try:
            revoked_token = TokenBlacklist(token=jti)
            db.session.add(revoked_token)
            db.session.commit()
            return jsonify({"msg": "Access token revoked"}), 200
        except:
            return jsonify({"msg": "Something went wrong"}), 500