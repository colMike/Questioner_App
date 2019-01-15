# """Meetup views File"""
# from flask import Blueprint, make_response, jsonify, request
# from app.api.v1.models.meetup_models import MeetupModels
# from app.api.v1.models.rsvp_models import RsvpModels


# rsvp_version1 = Blueprint('rsvp_version1', __name__, url_prefix='/api/v1')
# meetups = MeetupModels()
# reservations = RsvpModels()



# @rsvp_version1.route('/meetups/<meetupId>/rsvps', methods=['POST'])
# def retrieve_one_meetup(meetupId):
#     data = request.get_json()

#     reply = data["reply"]

#     if reply not in ["yes","no","maybe"]:
#         return make_response(jsonify({
#                 'status':400,
#                 'error':"You need to answer yes, no or maybe"
#             }),400)
#     meetup = meetups.get_one_meetup(meetupId)
#     if not meetup:
#         return make_response(jsonify({
#                 'status':404,
#                 'error':"Meetup does not exist"
#             }),404)
#     else:    

#         resp = reservations.make_reservation(reply)
#         return make_response(jsonify({
#             "Status": 200,
#             "data":{
#                 "meetup": meetupId,
#                 "topic": meetup['topic'],
#                 "Attendance": reply
#             }
#         }),200)

