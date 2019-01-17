"""question views File"""
from app.api.v2.models.question_models import QuestionModels
from app.api.v2.models.comment_models import CommentModels
from marshmallow import ValidationError
from flask import Blueprint, make_response, jsonify, request, abort
from ..Schemas.question_schema import QuestionSchema
from ..Schemas.comment_schema import CommentSchema

question_version2 = Blueprint(
    'question_version2', __name__, url_prefix='/api/v2')
questions = QuestionModels()
comments = CommentModels()

@question_version2.route('/questions', methods=['POST'])
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


@question_version2.route('/questions', methods=['GET'])
def retrieve_questions():
    """Return all questions"""
    all_questions = questions.get_all_questions()
    return make_response(jsonify({
        'status': 200,
        "data": all_questions,
        'message': "Success"
    }), 200)


@question_version2.route('/questions/<questionId>', methods=['GET'])
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


@question_version2.route('/questions/<int:questionId>/upvote', methods=['PATCH'])
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


@question_version2.route('/questions/<int:questionId>/downvote', methods=['PATCH'])
def downvote_question(questionId):
    voted_question = questions.downvote(questionId)

    print(voted_question)

    if not voted_question:
        return {
            "status": 404,
            "message": "Question does not exist"
        }, 404
    if voted_question['votes'] > 0:
        return make_response(jsonify({
            "status": 200,
            "data": voted_question,
            "message": "Downvote Successful"
        }), 200)
    else:
        abort(make_response(jsonify({
            "status": 403,
            "message": "Downvote Cannot go below 0"
        }), 403))        


@question_version2.route('/<questionId>/comments', methods=['POST'])
def post_comment(questionId):

    comment_data = request.get_json()

    data, errors = CommentSchema().load(comment_data)

    if errors:
        abort(make_response(jsonify({
            'status': 400,
            'message' : 'Invalid data. Please fill in a comment',
            'errors': errors}), 400))

    one_question = questions.get_one_question(questionId)
    
    if not one_question:
        abort(make_response(jsonify({
            'status': 400,
            'message': "No such question exists"
        }),400))

    questionId = one_question['questionId']
    title = one_question['title']
    body =  one_question['body']
    comment = data['comment']
    
    resp = comments.add_comment(questionId, title, body, comment)
    
    return make_response(jsonify({
            "status": 200,
            "data": resp,
            "message": "Comment registered in the system"
        }), 200)