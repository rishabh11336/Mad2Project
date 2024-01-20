from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity

from app.models.model import User, Cart, Order, OrderItem, db
from app.resources.auth.userAPI import custom_jwt_required

class OrderAPI(Resource):
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
        Cart = Cart.query.filter_by(user_id=current_user['id']).first()
        order = Order(
            user_id=current_user['id'],
            total_price=data['total_price']
            )
        db.session.add(order)
        db.session.flush()
        order_item = OrderItem(
            order_id=order.id,
            product_id=data['product_id'],
            product_name=data['product_name'],
            quantity=data['quantity'],
            price=data['price']
            )
        db.session.add(order_item)
        db.session.commit()
        


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