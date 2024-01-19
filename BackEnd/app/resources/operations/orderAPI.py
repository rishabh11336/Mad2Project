from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity

from app.models.model import User, Cart, Order, db
from app.resources.auth.userAPI import custom_jwt_required

class OrdeAPI(Resource):
    @custom_jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        orders = Order.query.filter_by(user_id=current_user['id'])
        if not orders:
            return jsonify({"msg": "Order not found"}), 404
        return jsonify([order.serialize() for order in orders]), 201
    

    @custom_jwt_required()
    def post(self):
        data = request.get_json()
        current_user = get_jwt_identity()
        user = User.query.filter_by(username=current_user['username']).first()
        if not user:
            return jsonify({"msg": "User not found"}), 404
        check = Order.query.filter_by(user_id=current_user['id']).first()
        if check:
            check.quantity = data['quantity']
            check.totalprice = data['totalprice']
            db.session.commit()
            return jsonify(check.serialize() | {'message':'order updated'}), 200
        order = Order(
            user_id=current_user['id'],
            quantity=data['quantity'],
            totalprice=data['totalprice']
            )
        db.session.add(order)
        db.session.commit()
        return jsonify(order.serialize() | {'message':'order created'}), 201

    
    @custom_jwt_required()
    def delete(self, id):
        current_user = get_jwt_identity()
        user = User.query.filter_by(username=current_user['username']).first()
        if not user:
            return jsonify({"msg": "User not found"}), 404
        order = Order.query.filter_by(id=id).first()
        if not order:
            return jsonify({"msg": "Order not found"}), 404
        db.session.delete(order)
        db.session.commit()
        return jsonify({"msg": "Order deleted"}), 200