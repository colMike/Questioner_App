"""Meetup views File"""
from flask import Blueprint, make_response, jsonify, request
from flask_restful import Resource

from app.api.v1.models.meetup_models import MeetupsModel


class MeetupList(Resource,MeetupsModel):
    """This is the meetup creation Model"""    
    
    def __init__(self):
        self.db = MeetupsModel()
    
    def post(self):
        """Method for Creating a new Meetup"""

        data = request.get_json()

        createdOn = data["createdOn"]
        location = data["location"]
        images = data["images"]
        topic = data["topic"]
        happeningOn = data["happeningOn"]
        tags = data["tags"]

        resp = self.db.add_meetup(createdOn, location, images, topic, happeningOn, tags)

        return make_response(jsonify({

            "data" : {
                    'Status': 201,
                    'Message': "Success"
                },
                "All Meetups": resp
            }), 201)

    
    def get(self):
        """Return all meetups"""
        all_meetups = self.db.get_all_meetups()
        return make_response(jsonify({
                "All Meetups": all_meetups,
                "data":{
                    'Status': "Okay",
                    'Message': "Success"
                }
            }), 200)

class Meetup(Resource, MeetupsModel):
    def __init__(self):
        self.db = MeetupsModel()

    
    def get(self, meetupId):
        """Return one meetup"""
        one_meetup = self.db.get_one_meetup(meetupId)
        return make_response(jsonify({
                "Meetup": one_meetup
            }), 200)

    def post(self, meetupId):
        """User response to a meetup (Yes, No, Maybe)"""

        data = request.get_json()

        reply = data["reply"]

        if reply not in ["yes","no","maybe"]:
            return make_response(jsonify({
                    'status':400,
                    'error':"You need to answer yes, no or maybe"
                }),400)
        meetup = self.db.get_one_meetup(meetupId)
        if not meetup:
            return make_response(jsonify({
                    'status':400,
                    'error':"Meetup does not exist"
                }),400)
        else:    
            return make_response(jsonify({
                "Status": 200,
                "data":{
                    "meetup": meetupId,
                    "topic": meetup['topic'],
                    "Attendance": reply

                }
            }),200)

