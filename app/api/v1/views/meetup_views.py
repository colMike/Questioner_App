"""Meetup views File"""
from flask import Blueprint, make_response, jsonify, request
from app.api.v1.models.meetup_models import MeetupModels
from app.api.v1.models.rsvp_models import RsvpModels


meetup_version1 = Blueprint('meetup_version1', __name__, url_prefix='/api/v1')
meetups = MeetupModels()
reservations = RsvpModels()


@meetup_version1.route('/meetups', methods=['POST'])
def create_meetup():
    """Method for Creating a new Meetup"""

    data = request.get_json()

    if isinstance(data["location"], str):
        if data["location"] != "":
            location = data["location"]
        else:
           return make_response(jsonify({
               'status': 404,
               'error': "Please enter some value for location"
           }), 404)
    else:
        return make_response(jsonify({
            'status': 404,
            'error': "Please enter an String as location"
        }), 404)

    images = data["images"]

    if isinstance(data["topic"], str):
        if data["topic"] != "":
            topic = data["topic"]
        else:
            return make_response(jsonify({
                'status': 404,
                'error': "Please enter a Topic"
            }), 404)
    else:
        return make_response(jsonify({
            'status': 404,
            'error': "Please enter a String data for the topic"
        }), 404)

    if isinstance(data["happeningOn"], str):
        if data["happeningOn"] != "":
            happeningOn = data["happeningOn"]
        else:
            return make_response(jsonify({
                'status': 404,
                'error': "Please enter some value for votes"
            }), 404)
    else:
        return make_response(jsonify({
            'status': 404,
            'error': "Please enter an Integer for votes"
        }), 404)

    tags = data["tags"]

    resp = meetups.add_meetup(location, images, topic, happeningOn, tags)

    return make_response(jsonify({
        'Status': 201,
        "Data": resp,
        'Message': "Question Posted Successfully"
    }), 201)


@meetup_version1.route('/meetups/upcoming', methods=['GET'])
def retrieve_meetups():
    """Return all meetups"""
    all_meetups = meetups.get_all_meetups()
    return make_response(jsonify({
        "All Meetups": all_meetups
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
        "Status": 200,
        "Question": one_meetup
    }), 200)


@meetup_version1.route('/meetups/<meetupId>/rsvps', methods=['POST'])
def post_rsvp(meetupId):

    data = request.get_json()

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

        resp = reservations.make_reservation(reply)
        
        return make_response(jsonify({
            "Status": 200,
            "Reply": resp
        }), 200)
