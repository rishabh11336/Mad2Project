from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity

from app.models.model import User, Cart, Order, Product, OrderItem, db
from app.resources.auth.userAPI import custom_jwt_required
from app.cache import cache


class OrderAPI(Resource):
    @custom_jwt_required()
    @cache.cached(timeout=300, query_string=True)
    def get(self):
        current_user = get_jwt_identity()
        orders = Order.query.filter_by(user_id=current_user['id'])
        if not orders:
            return jsonify({"msg": "Order not found"}), 404
        return jsonify([order.serialize() for order in orders]), 201
    

    @custom_jwt_required()
    def post(self):
        cache.clear()
        data = request.get_json()
        current_user = get_jwt_identity()
        user = User.query.filter_by(username=current_user['username']).first()
        if not user:
            return jsonify({"msg": "User not found"}), 404
        cart = Cart.query.filter_by(user_id=current_user['id']).all()
        if not cart:
            return jsonify({"msg": "Cart not found"}), 404
        new_order = Order(
            user_id=current_user['id'],
            quantity=sum([item["quantity"] for item in data['products']]),
            totalprice=data['total']
            )
        db.session.add(new_order)
        db.session.flush()
        order = Order.query.filter_by(user_id=current_user['id']).order_by(Order.id.desc()).first()
        for item in cart:
            orderItem = OrderItem(
                user_id=current_user['id'],
                order_id=order.id,
                product_id=item.product_id,
                product_name=item.product_name,
                quantity=item.quantity,
                price=item.price
                )
            update_product = Product.query.filter_by(id=item.product_id).first()
            update_product.quantity = update_product.quantity - item.quantity
            db.session.add(orderItem)
            db.session.delete(item)
            db.session.flush()
        db.session.commit()
        return jsonify(order.serialize() | {'message':'order created'}), 201
        


    @custom_jwt_required()
    def delete(self, id):
        cache.clear()
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