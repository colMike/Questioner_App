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
        }), 400))

    try:
        data = QuestionSchema().load(posted_data)
        createdBy = data["createdBy"]
        meetup = data["meetup"]
        title = data["title"]
        body = data["body"]

        resp = questions.add_question(createdBy, meetup, title, body)

        return make_response(jsonify({
            'status': 201,
            "data": resp,
            'message': "Question Posted Successfully"
        }), 201)

    except ValidationError as error:
        errors = error.messages

        if errors:
            abort(make_response(jsonify({
                'status': 400,
                'message': 'Invalid data. Please fill all required fields',
                'errors': errors}), 400))
    


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
    chosen_quiz = questions.get_one_question(questionId)
    
    if not chosen_quiz:
        return make_response(jsonify({
            'status': 404,
            'error': "Question does not exist"
        }), 404)


    result = questions.upvote(chosen_quiz[0])

    return make_response(jsonify({
        "status": 200,
        "data": result,
        "message": "Upvote Successful"
    }), 200)


@question_version2.route('/questions/<int:questionId>/downvote', methods=['PATCH'])
def downvote_question(questionId):

    chosen_quiz = questions.get_one_question(questionId)

    if not chosen_quiz:
            return make_response(jsonify({
                'status': 404,
                'error': "Question does not exist"
            }), 404)

    result = questions.downvote(chosen_quiz[0])

    if result:
        return make_response(jsonify({
            "status": 200,
            "data": result,
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

    try:
        data = CommentSchema().load(comment_data)
        one_question = questions.get_one_question(questionId)

        if not one_question:
            abort(make_response(jsonify({
                'status': 400,
                'message': "No such question exists"
            }), 400))

        questionId = one_question[0]
        title = one_question[4]
        body = one_question[5]
        comment = data['comment']

        resp = comments.add_comment(questionId, title, body, comment)

        return make_response(jsonify({
            "status": 200,
            "data": resp,
            "message": "Comment registered in the system"
        }), 200)

    except ValidationError as error:
       errors = error.messages
       if errors:
           abort(make_response(jsonify({
               'status': 400,
               'message': 'Invalid data. Please fill in a comment',
               'errors': errors}), 400))


