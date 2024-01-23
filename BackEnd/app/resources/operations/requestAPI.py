from flask_restful import Resource
from flask import request
from app.models.model import db, User, Product, Category
from flask_jwt_extended import get_jwt_identity
from app.resources.auth.userAPI import custom_jwt_required

# code added but not tested or used

class RequestAPI(Resource):
    secured = custom_jwt_required()

    # @secured
    def get(self):
        sm_requests = User.query.filter_by(role="store-manager", is_approved=0).all()
        return {
            "sm_requests": [sm_request.serialize() for sm_request in sm_requests]
        }, 200

    # @secured
    def post(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            user.is_approved = 1
            db.session.commit()
            return {"message": "Request approved"}, 201
        else:
            return {"message": "User not found"}, 404

    # @secured
    def delete(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            db.session.delete(user)
            db.session.commit()
            return {"message": "Request rejected"}, 200
        else:
            return {"message": "User not found"}, 404