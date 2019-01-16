"""Meetup views File"""
from flask import Blueprint, make_response, jsonify, request, abort
from marshmallow import ValidationError
from app.api.v1.models.meetup_models import MeetupModels
from ..Schemas.meetup_schema import MeetupSchema, RsvpSchema
from app.api.v1.models.rsvp_models import RsvpModels


meetup_version1 = Blueprint('meetup_version1', __name__, url_prefix='/api/v1')
meetups = MeetupModels()
reservations = RsvpModels()


@meetup_version1.route('/meetups', methods=['POST'])
def create_meetup():
    """Method for Creating a new Meetup"""

    posted_data = request.get_json()


    data, errors = MeetupSchema().load(posted_data)

    if errors:
        abort(make_response(jsonify({
            'status': 400,
            'message' : 'Invalid data. Please fill all required fields',
            'errors': errors}), 400))

    print(data)

    location = data["location"]
    images = data["images"]
    topic = data["topic"]
    happeningOn = data["happeningOn"]
    tags = data["tags"]

    resp = meetups.add_meetup(location, images, topic, happeningOn, tags)

    return make_response(jsonify({
        'status': 201,
        "data": resp,
        'message': "Meetup Added Successfully"
    }), 201)


@meetup_version1.route('/meetups/upcoming', methods=['GET'])
def retrieve_meetups():
    """Return all meetups"""
    all_meetups = meetups.get_all_meetups()
    return make_response(jsonify({
        "data": all_meetups,
        "status": 200
    }), 200)


@meetup_version1.route('/meetups/<meetupId>', methods=['GET'])
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


@meetup_version1.route('/meetups/<meetupId>/rsvps', methods=['POST'])
def post_rsvp(meetupId):

    meetup_data = request.get_json()

    if not meetup_data:
        abort(make_response(jsonify({
            'status': 400,
            'message': "No data has been provided"
        }),400))

    data, errors = RsvpSchema().load(meetup_data)

    if errors:
        abort(make_response(jsonify({
            'status': 400,
            'message' : 'Invalid data. Please fill all required fields',
            'errors': errors}), 400))

    reply = data["response"]


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

        resp = reservations.make_reservation(reply)
        
        return make_response(jsonify({
            "status": 200,
            "data": resp
        }), 200)
