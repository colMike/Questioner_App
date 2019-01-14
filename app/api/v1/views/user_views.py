"""User views File"""
from flask import Blueprint, make_response, jsonify, request
from flask_restful import Resource

from app.api.v1.models.user_models import UsersModel


class UserRegistration(Resource, UsersModel):
    """This is the User Registration Model"""

    def __init__(self):
        self.db = UsersModel()


    def post(self):
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

        resp = self.db.add_user(firstname, lastname, othername, email, phoneNumber, username, registered,isAdmin, password)
        
        return make_response(jsonify({
            'Status': "Ok",
            'Message': "Posted Successfully",
            'Current Order': resp
        }), 201)

    def get(self):
        """This is the GET route for all users in the data structure"""
        resp = self.db.get_users()
        return make_response(jsonify({
            'Status': "Okay",
            'Message': "Success",
            "All Users": resp
        }),201)


class UserLogin(Resource, UsersModel):
    """This is the User Signup Model"""
    
    def __init__(self):
        self.db = UsersModel()

    def post(self):

        data = request.get_json()

        username = data['username']
        password = data['password']

        sample_user = self.db.find_by_username(username)   
        passWrd = self.db.check_password(password)

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