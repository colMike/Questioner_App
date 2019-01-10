"""User views File"""
from flask import Blueprint, make_response, jsonify, request
from app.api.v1.models.user_models import UserModels

user_version1 = Blueprint('user_version1', __name__, url_prefix='/api/v1')
users = UserModels()


@user_version1.route('/auth/signup', methods=['POST'])

def signup():
    """Method for Registering user"""
    
    data = request.get_json()

    firstname = data['firstname']
    lastname = data['lastname']
    othername = data['othername']
    email = data['email']
    phoneNumber = data['phoneNumber']
    username = data['username']
    isAdmin = data['isAdmin']

    # user = users.add_user(username, email, password, confirm_password)

    return make_response(jsonify({
        # "status": 201,
        	"firstname": firstname,
	        "lastname": lastname,
	        "othername": othername,
            "email": email,
            "phoneNumber": phoneNumber,
            "username": username,
            "isAdmin": isAdmin
    }), 201)


@user_version1.route('/auth/login', methods=['POST'])

def login():
    """Method for Signing in a user"""
    
    data = request.get_json()

    username = data['username']
    password = data['password']

    user_one = users.find_username(username)
    passwrd = users.check_user_pwd(password)

    if not user_one:
        return make_response(jsonify({
            "User not found. Register for an account"
        }), 401)
    elif not passwrd:
        return make_response(jsonify({
            "Incorrect Password"
        }), 401)
    elif user_one and passwrd:
        return make_response(jsonify({
            "User": user_one
        }), 201)