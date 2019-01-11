"""Meetup views File"""
from flask import Blueprint, make_response, jsonify, request
from app.api.v1.models.meetup_models import MeetupModels

meetup_version1 = Blueprint('meetup_version1', __name__, url_prefix='/api/v1')
meetups = MeetupModels()


@meetup_version1.route('/meetups', methods=['POST'])
def create_meetup():
    """Method for Creating a new Meetup"""

    data = request.get_json()


    createdOn = data['createdOn']
    location = data['location']
    images = data['images']
    topic = data['topic']
    happeningOn = data['happeningOn']
    tags = data['tags']

    meetups.add_meetup(createdOn, location, images, topic, happeningOn, tags)

    return make_response(jsonify({

        "data" : {
            "createdOn": createdOn,
            "location": location,
            "images": images,
            "topic": topic, 
            "happeningOn": happeningOn,
            "tags": tags
            },
            "status": 201
        }), 201)
        
@meetup_version1.route('/meetups', methods=['GET'])
def retrieve_meetups():
    """Return all meetups"""
    all_meetups = meetups.get_all_meetups()
    return make_response(jsonify({
            "All Meetups": all_meetups
        }), 200)



