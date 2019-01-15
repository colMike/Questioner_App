"""question views File"""
from app.api.v1.models.question_models import QuestionModels
from flask import Blueprint, make_response, jsonify, request

question_version1 = Blueprint('question_version1', __name__, url_prefix='/api/v1')
questions = QuestionModels()


@question_version1.route('/questions', methods=['POST'])
def create_question():
    """Method for Creating a new question"""
    

    data = request.get_json()
        
    if isinstance(data["createdBy"], str):
        if data["createdBy"] != "":
            createdBy = data["createdBy"]
        else:
            return make_response(jsonify({
                'status': 404,
                'error': "CreatedBy cannot be left empty"
            }), 404)
    else:
        return make_response(jsonify({
            'status': 404,
            'error': "Please enter an String for CreatedBy"
        }), 404)
    if isinstance(data["meetup"], int):
        if data["meetup"] != "":
            meetup = data["meetup"]
        else:
           return make_response(jsonify({
               'status': 404,
               'error': "Please enter some value for meetup"
             }), 404)
    else:
        return make_response(jsonify({
            'status': 404,
            'error': "Please enter an Integer for meetup"
        }), 404)
    if isinstance(data["title"], str):
        if data["title"] != "":
            title = data["title"]
        else:
            return make_response(jsonify({
                'status': 404,
                'error': "Please enter some value for title"
            }), 404)
    else:
        return make_response(jsonify({
            'status': 404,
            'error': "Please enter a String for Title"
        }), 404)
    if isinstance(data["body"], str):
        if data["body"] != "":
            body = data["body"]
        else:
            return make_response(jsonify({
                'status': 404,
                'error': "Please enter some value for the Body"
            }), 404)
    else:
        return make_response(jsonify({
            'status': 404,
            'error': "Please enter a String for the body"
        }), 404)
    if isinstance(data["votes"], int):
        if data["votes"] != "":
            votes = data["votes"]
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
    
    resp = questions.add_question(createdBy, meetup, title, body, votes)

    return make_response(jsonify({
        'Status': 201,
        "Data": resp,
        'Message': "Question Posted Successfully"
    }), 201)
    
    
   
        # .....................................
@question_version1.route('/questions', methods=['GET'])
def retrieve_questions():
    """Return all questions"""
    all_questions = questions.get_all_questions()
    return make_response(jsonify({
            'Status': 200,
            "Data": all_questions,
            'Message': "Success"
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
            "Status": 200,
            "Question": one_question
        }), 200)

@question_version1.route('/questions/<questionId>/upvote', methods=['PATCH'])
def upvote_question(questionId):
    voted_question = questions.upvote(questionId)
    if not voted_question:
        return {
            "status": 404,
            "Message": "Question does not exist"
        }, 404
    return make_response(jsonify({
        "Status": 200,
        "Data": voted_question,
        "message": "Upvote Successful"
    }), 200)


@question_version1.route('/questions/<questionId>/downvote', methods=['PATCH'])
def downvote_question(questionId):
    voted_question = questions.downvote(questionId)
    if not voted_question:
        return {
            "status": 404,
            "Message": "Question does not exist"
        }, 404
    return make_response(jsonify({
        "Status": 200,
        "Data": voted_question,
        "message": "Upvote Successful"
    }), 200)


