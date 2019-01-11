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
    registered = data['registered']
    isAdmin = data['isAdmin']
    password = data['password']

    users.add_user(firstname, lastname, othername, email, phoneNumber, username, registered, isAdmin, password)

    return make_response(jsonify({
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

    sample_user = users.find_by_username(username)   
    passWrd = users.check_password(password)
    if not sample_user:
        return make_response(jsonify({
            "Error": "User not found: Please register"
        }), 401)
    elif not passWrd:
        return make_response(jsonify({
            "Error": "Password incorrect"
        }), 401)
    elif sample_user and passWrd:
        return make_response(jsonify({
                        "username": username,
                        "password": password
                        }), 201)