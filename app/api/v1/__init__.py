from .views.user_views import UserRegistration, UserLogin
from .views.meetup_views import MeetupList, Meetup
from .views.question_views import QuestionList, Question, QuestionDownvote

from flask_restful import Api, Resource
from flask import Blueprint

version_one = Blueprint('api_v1', __name__,url_prefix="/api/v1")
api = Api(version_one)

api.add_resource(UserRegistration, "/auth/users/signup")
api.add_resource(UserLogin, "/auth/users/login")
api.add_resource(MeetupList, "/meetups")
api.add_resource(Meetup, "/meetups/<meetupId>", 
                        "/meetups/<meetupId>/rsvps")
api.add_resource(QuestionList, "/questions")
api.add_resource(Question, "/questions/<questionId>",
                            "/questions/<questionId>/upvote")
api.add_resource(QuestionDownvote, "/questions/<questionId>/downvote")
