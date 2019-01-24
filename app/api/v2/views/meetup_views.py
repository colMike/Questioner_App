"""Meetup views File"""
from flask import Blueprint, make_response, jsonify, request, abort
from marshmallow import ValidationError
from app.api.v2.models.meetup_models import MeetupModels
from app.api.v2.models.user_models import UserModels
from flask_jwt_extended import (get_jwt_identity, jwt_required)
from ..Schemas.meetup_schema import MeetupSchema, RsvpSchema
from app.api.v2.models.rsvp_models import RsvpModels


meetup_version2 = Blueprint('meetup_version2', __name__, url_prefix='/api/v2')
meetups = MeetupModels()
reservations = RsvpModels()
users = UserModels()


@meetup_version2.route('/meetups', methods=['POST'])
@jwt_required
def create_meetup():
    """Method for Creating a new Meetup"""
    posted_data = request.get_json()


    username = get_jwt_identity()
        
    user = users.get_user(username)
    
    if user != "admin":
        abort(make_response(jsonify({
                'status': 400,
                'Error': 'You have to be an Admin to post a meetup'
                }), 400))           

    else:
        try:
            data = MeetupSchema().load(posted_data)

            location = data["location"]
            meetup_images = data["meetup_images"]
            topic = data["topic"]
            happeningOn = data["happeningOn"]
            meetup_tags = data["meetup_tags"]
            description = data["description"]

            resp = meetups.add_meetup(
                location, meetup_images, topic, happeningOn, meetup_tags, description)

            if not resp:
                return make_response(jsonify({
                    'message': "Meetup Already exists"
            }), 201)
            else:
                return make_response(jsonify({
                    'status': 201,
                    "data": resp,
                    'message': "Meetup Added Successfully"
                }), 201)

        except ValidationError as error:
            errors = error.messages

            if errors:
                abort(make_response(jsonify({
                    'status': 400,
                    'message': 'Invalid data. Please fill all required fields',
                    'errors': errors}), 400))


@meetup_version2.route('/meetups/upcoming', methods=['GET'])
def retrieve_meetups():
    """Return all meetups"""
    all_meetups = meetups.get_all_meetups()
    return make_response(jsonify({
        "data": all_meetups,
        "status": 200
    }), 200)


@meetup_version2.route('/meetups/<meetupId>', methods=['GET'])
def retrieve_one_meetup(meetupId):
    """Return one meetup"""
    one_meetup = meetups.get_one_meetup(meetupId)
    if not one_meetup:
        return make_response(jsonify({
            'status': 404,
            'error': "Meetup does not exist"
        }), 404)
    return make_response(jsonify({
        "status": 200,
        "message": "Success",
        "data": one_meetup
    }), 200)


@meetup_version2.route('/meetups/<meetupId>/rsvps', methods=['POST'])
def post_rsvp(meetupId):

    meetup_data = request.get_json()

    if not meetup_data:
        abort(make_response(jsonify({
            'status': 400,
            'message': "No data has been provided"
        }), 400))

    try:

        data = RsvpSchema().load(meetup_data)

        reply = data["reply"]

        if reply not in ["yes", "no", "maybe"]:
            return make_response(jsonify({
                'status': 400,
                'error': "You need to answer yes, no or maybe"
            }), 400)

        meetup = meetups.get_one_meetup(meetupId)

        if not meetup:
            return make_response(jsonify({
                'status': 404,
                'error': "Meetup does not exist"
            }), 404)
        else:

            resp = reservations.make_reservation(reply, meetup[0])

            return make_response(jsonify({
                "status": 200,
                "data": resp
            }), 200)

    except ValidationError as error:

       errors = error.messages
       if errors:
           abort(make_response(jsonify({
               'status': 400,
               'message': 'Invalid data. Please fill all required fields',
               'errors': errors}), 400))


@meetup_version2.route('/meetups/<meetupId>', methods=['DELETE'])
@jwt_required
def delete_meetup(meetupId):
    """Return one meetup"""

    username = get_jwt_identity()
        
    user = users.get_user(username)
    
    if user != "admin":
        abort(make_response(jsonify({
                'status': 400,
                'Error': 'You have to be an Admin to DELETE a meetup'
                }), 400))           

    one_meetup = meetups.get_one_meetup(meetupId)
    if not one_meetup:
        return make_response(jsonify({
            'status': 404,
            'error': "Meetup does not exist"
        }), 404)

    meetups.delete(meetupId)

    return make_response(jsonify({
        "status": 200,
        "message": "DELETED MEETUP"
    }), 200)

