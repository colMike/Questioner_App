"""question views File"""
from flask import Blueprint, make_response, jsonify, request
from flask_restful import Resource

from app.api.v1.models.question_models import QuestionsModel


class QuestionList(Resource, QuestionsModel):
    """Class for managing entire Questions List"""
    def __init__(self):
        self.db = QuestionsModel()


    def post(self):
        """Method for Creating a new question"""

        data = request.get_json()

        createdOn = data["createdOn"]
        createdBy = data["createdBy"]
        meetup = data["meetup"]
        title =   data["title"]
        body =   data["body"]
        votes = data["votes"]

        resp = self.db.add_question(createdOn, createdBy, meetup, title, body, votes)

        return make_response(jsonify({
            "All questions": resp,
            "data":{
                'Status': "Okay",
                'Message': "Question Posted Successfully"
            }
        }), 201)

                
    
    def get(self):
        """Return all questions"""
        all_questions = self.db.get_all_questions()
        return make_response(jsonify({
            "All questions": all_questions,
            "data":{
                'Status': "Okay",
                'Message': "Success"
            }
            }), 200)


class Question(Resource, QuestionsModel):
    """Class for managing a single question"""
    def __init__(self):
        self.db = QuestionsModel()

    
    def get(self, questionId):
        """Return one question"""
        one_question = self.db.get_one_question(questionId)
        return make_response(jsonify({
                "Question": one_question
            }), 200)


    # Upvote a Question
    def patch(self, questionId):
        "Upvote or downvote a question"

        question = self.db.upvote(questionId)
        if not question:
            return {
                "Error": "Question does not exist",
                "status": 404
            }, 404
        return {
            
            "message": "Upvote Successful",
            "Question": question
        }, 200

class QuestionDownvote(Resource, QuestionsModel):
    def __init__(self):
        self.db = QuestionsModel()

    # Downvote a Question
    def patch(self, questionId):
        "Upvote or downvote a question"

        question = self.db.downvote(questionId)
        if not question:
            return {
                "Error": "Question does not exist",
                "status": 404
            }, 404
        return {            
            "message": "Upvote Successful",
            "Question": question
        }, 200


