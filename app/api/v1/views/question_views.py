"""question views File"""
from app.api.v1.models.question_models import QuestionModels
from marshmallow import ValidationError
from flask import Blueprint, make_response, jsonify, request, abort
from ..Schemas.question_schema import QuestionSchema

question_version1 = Blueprint(
    'question_version1', __name__, url_prefix='/api/v1')
questions = QuestionModels()


@question_version1.route('/questions', methods=['POST'])
def create_question():
    """Method for Creating a new question"""

    posted_data = request.get_json()

    if not posted_data:
        abort(make_response(jsonify({
            'status': 400,
            'message': "No data has been provided"
        }),400))

    data, errors = QuestionSchema().load(posted_data)

    if errors:
        abort(make_response(jsonify({
            'status': 400,
            'message' : 'Invalid data. Please fill all required fields',
            'errors': errors}), 400))

    createdBy = data["createdBy"]
    meetup = data["meetup"]
    title = data["title"]
    body = data["body"]
    votes = data["votes"]
       	            
    resp = questions.add_question(createdBy, meetup, title, body, votes)

    return make_response(jsonify({
        'status': 201,
        "data": resp,
        'message': "Question Posted Successfully"
    }), 201)


@question_version1.route('/questions', methods=['GET'])
def retrieve_questions():
    """Return all questions"""
    all_questions = questions.get_all_questions()
    return make_response(jsonify({
        'status': 200,
        "data": all_questions,
        'message': "Success"
    }), 200)


@question_version1.route('/questions/<questionId>', methods=['GET'])
def get_question(questionId):
        """Return one question"""
        one_question = questions.get_one_question(questionId)
        if not one_question:
            return make_response(jsonify({
                'status': 404,
                'error': "Question does not exist"
            }), 404)
        return make_response(jsonify({
            "status": 200,
            "data": one_question
        }), 200)


@question_version1.route('/questions/<int:questionId>/upvote', methods=['PATCH'])
def upvote_question(questionId):
    voted_question = questions.upvote(questionId)
    if not voted_question:
        return {
            "status": 404,
            "message": "Question does not exist"
        }, 404
    return make_response(jsonify({
        "status": 200,
        "data": voted_question,
        "message": "Upvote Successful"
    }), 200)


@question_version1.route('/questions/<int:questionId>/downvote', methods=['PATCH'])
def downvote_question(questionId):
    voted_question = questions.downvote(questionId)
    if not voted_question:
        return {
            "status": 404,
            "message": "Question does not exist"
        }, 404
    return make_response(jsonify({
        "status": 200,
        "data": voted_question,
        "message": "Upvote Successful"
    }), 200)
