from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from datetime import datetime

from app.models.model import User, Product, db
from app.resources.auth.userAPI import custom_jwt_required


class ProductAPI(Resource):
    @custom_jwt_required()
    def get(self, id=None):
        if id:
            product = Product.query.filter_by(id=id).first()
            if not product:
                return jsonify({"msg": "Product not found"}), 404
            return jsonify(product.serialize())
        products = Product.query.filter_by()
        return jsonify([product.serialize() for product in products if product.approved])
    
    @custom_jwt_required()
    def post(self):
        data = request.get_json()
        current_user = get_jwt_identity()
        storeManager = User.query.filter_by(username=current_user['username'], role='storemanager').first()
        admin = User.query.filter_by(username=current_user['username'], role='admin').first()
        if not (storeManager or admin):
            return jsonify({"msg": "User not found"}), 404
        best_before_str = data['best_before']
        # best_before_date = datetime.strptime(best_before_str, "%a, %d %b %Y %H:%M:%S %Z")
        best_before_date = datetime.strptime(best_before_str, "%Y-%m-%d")
        product = Product(
            name=data['name'],
            image=data['image'],
            price=data['price'],
            quantity=data['quantity'],
            si_unit=data['si_unit'],
            best_before=best_before_date,
            category_id=data['category_id'],
            createdBy=current_user['id'],
            approved=True if admin else False)
        db.session.add(product)
        db.session.commit()
        return jsonify(product.serialize() | {'message':'product created'}), 201
    
    @custom_jwt_required()
    def put(self, id):
        data = request.get_json()
        current_user = get_jwt_identity()
        best_before_str = data['best_before']
        # best_before_date = datetime.strptime(best_before_str, "%a, %d %b %Y %H:%M:%S %Z")
        best_before_date = datetime.strptime(best_before_str, "%Y-%m-%d")
        storeManager = User.query.filter_by(username=current_user['username'], role='storemanager').first()
        admin = User.query.filter_by(username=current_user['username'], role='admin').first()
        if not (storeManager or admin):
            return jsonify({"msg": "User not found"}), 404
        product = Product.query.filter_by(id=id).first()
        if not product:
            return jsonify({"msg": "Product not found"}), 404
        product.name = data['name']
        product.image = data['image']
        product.price = data['price']
        product.quantity = data['quantity']
        product.si_unit = data['si_unit']
        product.best_before = best_before_date
        product.category_id = data['category_id']
        product.createdBy = current_user['id']
        if not admin:
            product.approved = False
        db.session.commit()
        return jsonify(product.serialize() | {'message':'product updated'}), 201
    
    @custom_jwt_required()
    def delete(self, id):
        current_user = get_jwt_identity()
        storeManager = User.query.filter_by(username=current_user['username'], role='storemanager').first()
        admin = User.query.filter_by(username=current_user['username'], role='admin').first()
        if not (storeManager or admin):
            return jsonify({"msg": "User not found"}), 404
        product = Product.query.filter_by(id=id).first()
        if not product:
            return jsonify({"msg": "Product not found"}), 404
        if storeManager:
            product.approved = False
            return jsonify({"msg": "Unauthorized"}), 401
        db.session.delete(product)
        db.session.commit()
        return jsonify({"msg": "Product deleted"}), 200