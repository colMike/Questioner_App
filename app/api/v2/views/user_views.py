"""User views File"""
from flask import Flask, Blueprint, make_response, jsonify, request, abort
from app.api.v1.models.user_models import UserModels
from marshmallow import ValidationError
import jwt
import datetime
from ..Schemas.user_schema import UserSignupSchema, UserLoginSchema


user_version1 = Blueprint('user_version1', __name__, url_prefix='/api/v1')
users = UserModels()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is my secret Key' 

@user_version2.route('/auth/signup', methods=['POST'])
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
        
        token = jwt.encode({'username' : username, 
                            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes = 60)}, app.config['SECRET_KEY'])
        
        resp = users.add_user(firstname, lastname, othername,
                              email, phoneNumber, username, password)

        return make_response(jsonify({
            'status': 201,
            "data": [{'token' : token.decode('UTF-8'), 'user' : resp}],
            'message': "User Added Successfully"
        }), 201)


<<<<<<< HEAD
@user_version2.route('/auth/login', methods=['POST'])
=======
@user_version1.route('/auth/login', methods=['POST'])
>>>>>>> b49380a025865d072e7d0976c68626b855cd093d
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

        token = jwt.encode({'username' : username, 
                            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes = 60)}, app.config['SECRET_KEY'])

        return make_response(jsonify({
            'status': 201,
            "data": [{'token' : token.decode('UTF-8'), 'userName' : username}],
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

