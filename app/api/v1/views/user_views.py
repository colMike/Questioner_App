"""User views File"""
from flask import Blueprint, make_response, jsonify, request
from app.api.v1.models.user_models import UserModels

user_version1 = Blueprint('user_version1', __name__, url_prefix='/api/v1')
users = UserModels()


@user_version1.route('/auth/signup', methods=['POST'])
def signup():
    """Method for Registering user"""
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    confirm_password = data['confirm_password']

    
    return make_response(jsonify({
        "message": "successful registration"
    }), 201)