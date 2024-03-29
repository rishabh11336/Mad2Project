from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity

from app.models.model import User, Category, db
from app.resources.auth.userAPI import custom_jwt_required
from app.cache import cache

class CategoryAPI(Resource):

    @custom_jwt_required()
    @cache.cached(timeout=300, query_string=True)
    def get(self, id=None):
        if id:
            category = Category.query.filter_by(id=id).first()
            if not category:
                return jsonify({"msg": "Category not found"}), 404
            return jsonify(category.serialize())
        categories = Category.query.filter_by()
        return jsonify([category.serialize() for category in categories if category.approved])
    
    @custom_jwt_required()
    def post(self):
        cache.clear()
        data = request.get_json()
        current_user = get_jwt_identity()
        storeManager = User.query.filter_by(username=current_user['username'], role='storemanager').first()
        admin = User.query.filter_by(username=current_user['username'], role='admin').first()
        if not (storeManager or admin):
            return jsonify({"msg": "User not found"}), 404
        category = Category(
            name=data['name'],
            description=data['description'],
            image=data['image'],
            createdBy=current_user['id'],
            approved=True if admin else False)
        db.session.add(category)
        db.session.commit()
        return jsonify(category.serialize() | {'message':'category created'}), 201
    
    @custom_jwt_required()
    def put(self, id):
        cache.clear()
        data = request.get_json()
        current_user = get_jwt_identity()
        storeManager = User.query.filter_by(username=current_user['username'], role='storemanager').first()
        admin = User.query.filter_by(username=current_user['username'], role='admin').first()
        if not (storeManager or admin):
            return jsonify({"msg": "User not found"}), 404
        category = Category.query.filter_by(id=id).first()
        if not category:
            return jsonify({"msg": "Category not found"}), 404
        category.name = data['name']
        category.description = data['description']
        category.image = data['image']
        category.createdBy = current_user['id']
        if not admin:
            category.approved = False
        db.session.commit()
        return jsonify(category.serialize() | {'message':'category updated'}), 200
    
    @custom_jwt_required()
    def delete(self, id):
        cache.clear()
        current_user = get_jwt_identity()
        storeManager = User.query.filter_by(username=current_user['username'], role='storemanager').first()
        admin = User.query.filter_by(username=current_user['username'], role='admin').first()
        if not (storeManager or admin):
            return jsonify({"msg": "User not found"}), 404
        category = Category.query.filter_by(id=id).first()
        if not category:
            return jsonify({"msg": "Category not found"}), 404
        if storeManager:
            category.approved = False
            db.session.commit()
            return jsonify({"msg": "Category updated"}), 200
        db.session.delete(category)
        db.session.commit()
        return jsonify({"msg": "Category deleted"}), 200