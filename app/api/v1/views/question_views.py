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

        if isinstance(data["createdOn"], str):
            if  data["createdOn"] != "":
                createdOn = data["createdOn"]
            else:
                return make_response(jsonify({
                    'status':404,
                    'error':"Please enter some value at created on"
                }),404)
        else:
            return make_response(jsonify({
                    'status':404,
                    'error':"Please enter a String for createdOn"
            }),404)

        if isinstance(data["createdBy"], str):
            if  data["createdBy"] != "":
                createdBy = data["createdBy"]
            else:
                return make_response(jsonify({
                    'status':404,
                    'error':"CreatedBy cannot be left empty"
                }),404)
        else:
            return make_response(jsonify({
                    'status':404,
                    'error':"Please enter an String for CreatedBy"
            }),404)        

        if isinstance(data["meetup"], int):
            if  data["meetup"] != "":
                meetup = data["meetup"]
            else:
                return make_response(jsonify({
                    'status':404,
                    'error':"Please enter some value for meetup"
                }),404)
        else:
            return make_response(jsonify({
                    'status':404,
                    'error':"Please enter an Integer for meetup"
            }),404)        

        if isinstance(data["title"], str):
            if  data["title"] != "":
                title = data["title"]
            else:
                return make_response(jsonify({
                    'status':404,
                    'error':"Please enter some value for title"
                }),404)
        else:
            return make_response(jsonify({
                    'status':404,
                    'error':"Please enter a String for Title"
            }),404)        

        if isinstance(data["body"], str):
            if  data["body"] != "":
                body = data["body"]
            else:
                return make_response(jsonify({
                    'status':404,
                    'error':"Please enter some value for the Body"
                }),404)
        else:
            return make_response(jsonify({
                    'status':404,
                    'error':"Please enter a String for the body"
            }),404)        
        
        if isinstance(data["votes"], int):
            if  data["votes"] != "":
                votes = data["votes"]
            else:
                return make_response(jsonify({
                    'status':404,
                    'error':"Please enter some value for votes"
                }),404)
        else:
            return make_response(jsonify({
                    'status':404,
                    'error':"Please enter an Integer for votes"
            }),404)

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
        if not one_question:
            return make_response(jsonify({
                    'status':404,
                    'error':"Question does not exist"
                }),404)
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




