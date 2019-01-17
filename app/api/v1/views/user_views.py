"""User views File"""
from flask import Blueprint, make_response, jsonify, request, abort
from app.api.v1.models.user_models import UserModels
from marshmallow import ValidationError
from ..Schemas.user_schema import UserSignupSchema, UserLoginSchema


user_version1 = Blueprint('user_version1', __name__, url_prefix='/api/v1')
users = UserModels()


@user_version1.route('/auth/users/signup', methods=['POST'])
def signup():
    """Method for Registering user"""

    signup_data = request.get_json()

    if not signup_data:
        abort(make_response(jsonify({
            'status': 400,
            'message': "No data has been provided"
        }),400))

    data, errors = UserSignupSchema().load(signup_data)

    if errors:
        abort(make_response(jsonify({
            'status': 400,
            'message' : 'Invalid data. Please fill all required fields',
            'errors': errors}), 400))
            
    

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
        resp = users.add_user(firstname, lastname, othername,
                              email, phoneNumber, username, password)

        return make_response(jsonify({
            'status': 201,
            "data": resp,
            'message': "User Added Successfully"
        }), 201)


@user_version1.route('/auth/users/login', methods=['POST'])
def login():
    """Method for Signing in a user"""

    user_data = request.get_json()

    if not user_data:
        abort(make_response(jsonify({
            'status': 400,
            'message': "No data has been provided"
        }),400))

    data, errors = UserLoginSchema().load(user_data)

    if errors:
        abort(make_response(jsonify({
            'status': 400,
            'message' : 'Invalid data. Please fill all required fields',
            'errors': errors}), 400))
            
    
    username = data['username']
    password = data['password']

    sample_user = users.find_by_username(username)
    passWrd = users.check_password(password)
    if not sample_user:
        return make_response(jsonify({
            "error": "User not found: Please register"
        }), 401)
    elif not passWrd:
        return make_response(jsonify({
            "error": "Password incorrect"
        }), 401)
    elif sample_user and passWrd:
        return make_response(jsonify({
            'status': 201,
            "data": {
                "username": username,
                "password": password
            },
            'message': "User Logged in Successfully"
        }), 201)
    
@user_version1.route('/users', methods=['GET'])
def retrieve_users():
    """Return all Users"""
    all_users = users.get_all_users()
    return make_response(jsonify({
        "data": all_users,
        "status": 200
    }), 200)

