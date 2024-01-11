from flask import request, jsonify
from flask_restful import Resource
# from flask_jwt_extended import jwt_required, get_jwt_identity
# from flask_jwt_extended import create_access_token, create_refresh_token
# from flask_jwt_extended import jwt_refresh_token_required, get_raw_jwt
# from werkzeug.security import safe_str_cmp
from app.models.model import User, db



class UserAPI(Resource):
    def get(self, id=None):
        if id:
            user = User.query.filter_by(id=id).first()
            if not user:
                return jsonify({"msg": "User not found"}), 404
            return jsonify(user.serialize())
        users = User.query.all()
        return jsonify([e.serialize() for e in users])
    
class RegisterAPI(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user:
            return jsonify({"msg": "User already exists"}), 400
        user = User(
            username=data['username'],
            password=data['password'],
            role='user',
            email=data['email'],
            approved=True)
        db.session.add(user)
        db.session.commit()
        return jsonify(user.serialize() | {'message':'user registered'}), 201
    