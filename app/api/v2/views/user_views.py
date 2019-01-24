"""User views File"""
import os
from flask import Flask, Blueprint, make_response, jsonify, request, abort
from app.api.v2.models.user_models import UserModels
import jwt
from flask_jwt_extended import (create_access_token)
import datetime
from ..Schemas.user_schema import UserSignupSchema, UserLoginSchema
from marshmallow import ValidationError


user_version2 = Blueprint('user_version2', __name__, url_prefix='/api/v2')
users = UserModels()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET")

@user_version2.route('/auth/signup', methods=['POST'])
def signup():
    """Method for Registering user"""

    signup_data = request.get_json()

    if not signup_data:
        abort(make_response(jsonify({
            'status': 400,
            'message': "No data has been provided"
        }), 400))

    try:
        data = UserSignupSchema().load(signup_data)

        firstname = data['firstname']
        lastname = data['lastname']
        othername = data['othername']
        email = data['email']
        phoneNumber = data['phoneNumber']
        username = data['username']
        password = data['password']

        if users.check_exists(data["username"], data["email"]):
            abort(make_response(jsonify({
                'status': 403,
                'message': "User Already exists"
            }), 403))
        else:

            token = create_access_token(identity=username)

            payload = users.add_user(firstname, lastname, othername,
                                     email, phoneNumber, username, password)

            return make_response(jsonify({
                'status': 201,
                "data": {'user': payload},
                'message': "User Added Successfully"
            }), 201)

    except ValidationError as error:
        errors = error.messages
        if errors:
            abort(make_response(jsonify({
                'status': 400,
                'message': 'Invalid data. Please fill all required fields',
                'errors': errors}), 400))


@user_version2.route('/auth/login', methods=['POST'])
def login():
    """Method for Signing in a user"""

    user_data = request.get_json()

    if not user_data:
        abort(make_response(jsonify({
            'status': 400,
            'message': "No data has been provided"
        }), 400))

    try:
        data = UserLoginSchema().load(user_data)
        username = data['username']
        password = data['password']
        sample_user = users.find_by_username(username)

        passWrd = users.check_password(username, password)

        if not sample_user:
            abort(make_response(jsonify({
                'status': 401,
                'error': "User not found: Please register"
            }), 401))
        else:
            if not passWrd:
                abort(make_response(jsonify({
                    'status': 401,
                    'error': "Password incorrect"
                }), 401))

            elif passWrd:

                # token = jwt.encode({'username': username,
                #                     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])    
                token = create_access_token(identity=username)

                return make_response(jsonify({
                    'status': 201,
                    "data": {"Token": token, 'username': username},
                    'message': "User Logged in Successfully"
                }), 201)

    except ValidationError as error:
        errors = error.messages
        if errors:
            abort(make_response(jsonify({
                'status': 400,
                'message': 'Invalid data. Please fill all required fields',
                'errors': errors}), 400))


@user_version2.route('/users', methods=['GET'])
def retrieve_users():
    """Return all Users"""
    all_users = users.get_all_users()

    return make_response(jsonify({
        "data": all_users,
        "status": 200
    }), 200)

