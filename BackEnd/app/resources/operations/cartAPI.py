from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity

from app.models.model import User, Cart, db
from app.resources.auth.userAPI import custom_jwt_required

class CartAPI(Resource):
    @custom_jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        carts = Cart.query.filter_by(user_id=current_user['id'])
        if not carts:
            return jsonify({"msg": "Cart not found"}), 404
        return jsonify([cart.serialize() for cart in carts])
        
    
    @custom_jwt_required()
    def post(self):
        data = request.get_json()
        current_user = get_jwt_identity()
        user = User.query.filter_by(username=current_user['username']).first()
        if not user:
            return jsonify({"msg": "User not found"}), 404
        check = Cart.query.filter_by(user_id=current_user['id'], product_id=data['product_id']).first()
        if check:
            check.quantity = data['quantity']
            db.session.commit()
            return jsonify(check.serialize() | {'message':'cart updated'}), 200
        cart = Cart(
            user_id=current_user['id'],
            product_id=data['product_id'],
            product_name=data['product_name'],
            quantity=data['quantity'],
            price=data['price']
            )
        db.session.add(cart)
        db.session.commit()
        return jsonify(cart.serialize() | {'message':'cart created'}), 201
    
    @custom_jwt_required()
    def delete(self, id):
        current_user = get_jwt_identity()
        user = User.query.filter_by(username=current_user['username']).first()
        if not user:
            return jsonify({"msg": "User not found"}), 404
        cart = Cart.query.filter_by(id=id).first()
        if not cart:
            return jsonify({"msg": "Cart not found"}), 404
        db.session.delete(cart)
        db.session.commit()
        return jsonify({"msg": "Cart deleted"}), 200