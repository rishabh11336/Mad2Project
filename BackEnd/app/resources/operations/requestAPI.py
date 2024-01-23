from flask_restful import Resource
from flask import request, jsonify
from app.models.model import db, User, Product, Category
from flask_jwt_extended import get_jwt_identity
from app.resources.auth.userAPI import custom_jwt_required


class AdminProductRequestAPI(Resource):
    @custom_jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        admin = User.query.filter_by(username=current_user['username'], role='admin').first()
        if not admin:
            return jsonify({"msg": "User not found"}), 404
        products = Product.query.filter_by(approved=False)
        return jsonify([product.serialize() for product in products]), 201
    
    @custom_jwt_required()
    def put(self, id):
        data = request.get_json()
        current_user = get_jwt_identity()
        admin = User.query.filter_by(username=current_user['username'], role='admin').first()
        if not admin:
            return jsonify({"msg": "User not found"}), 404
        product = Product.query.filter_by(id=id).first()
        if not product:
            return jsonify({"msg": "Product not found"}), 404
        product.approved = data['approved']
        db.session.commit()
        return jsonify({"msg": "Product updated"}), 201
    
    @custom_jwt_required()
    def delete(self, id):
        current_user = get_jwt_identity()
        admin = User.query.filter_by(username=current_user['username'], role='admin').first()
        if not admin:
            return jsonify({"msg": "User not found"}), 404
        product = Product.query.filter_by(id=id).first()
        if not product:
            return jsonify({"msg": "Product not found"}), 404
        db.session.delete(product)
        db.session.commit()
        return jsonify({"msg": "Product deleted"}), 201
    
class AdminCategoryRequest(Resource):
    @custom_jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        admin = User.query.filter_by(username=current_user['username'], role='admin').first()
        if not admin:
            return jsonify({"msg": "User not found"}), 404
        categories = Category.query.filter_by(approved=False)
        return jsonify([category.serialize() for category in categories]), 201
    
    @custom_jwt_required()
    def put(self, id):
        data = request.get_json()
        current_user = get_jwt_identity()
        admin = User.query.filter_by(username=current_user['username'], role='admin').first()
        if not admin:
            return jsonify({"msg": "User not found"}), 404
        category = Category.query.filter_by(id=id).first()
        if not category:
            return jsonify({"msg": "Category not found"}), 404
        category.approved = data['approved']
        db.session.commit()
        return jsonify({"msg": "Category updated"}), 201

    @custom_jwt_required()
    def delete(self, id):
        current_user = get_jwt_identity()
        admin = User.query.filter_by(username=current_user['username'], role='admin').first()
        if not admin:
            return jsonify({"msg": "User not found"}), 404
        category = Category.query.filter_by(id=id).first()
        if not category:
            return jsonify({"msg": "Category not found"}), 404
        db.session.delete(category)
        db.session.commit()
        return jsonify({"msg": "Category deleted"}), 201
    
class AdminStoreManagerRequest(Resource):
    @custom_jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        admin = User.query.filter_by(username=current_user['username'], role='admin').first()
        if not admin:
            return jsonify({"msg": "User not found"}), 404
        storeManagers = User.query.filter_by(role='storemanager', approved=False)
        return jsonify([storeManager.serialize() for storeManager in storeManagers]), 201
    
    @custom_jwt_required()
    def put(self, id):
        data = request.get_json()
        current_user = get_jwt_identity()
        admin = User.query.filter_by(username=current_user['username'], role='admin').first()
        if not admin:
            return jsonify({"msg": "User not found"}), 404
        storeManager = User.query.filter_by(id=id).first()
        if not storeManager:
            return jsonify({"msg": "Store Manager not found"}), 404
        storeManager.approved = data['approved']
        db.session.commit()
        return jsonify({"msg": "Store Manager updated"}), 201
    
    @custom_jwt_required()
    def delete(self, id):
        current_user = get_jwt_identity()
        admin = User.query.filter_by(username=current_user['username'], role='admin').first()
        if not admin:
            return jsonify({"msg": "User not found"}), 404
        storeManager = User.query.filter_by(id=id).first()
        if not storeManager:
            return jsonify({"msg": "Store Manager not found"}), 404
        db.session.delete(storeManager)
        db.session.commit()
        return jsonify({"msg": "Store Manager deleted"}), 201