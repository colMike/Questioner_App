"""question views File"""
from app.api.v1.models.question_models import QuestionModels
from flask import Blueprint, make_response, jsonify, request

question_version1 = Blueprint('question_version1', __name__, url_prefix='/api/v1')
questions = QuestionModels()


@question_version1.route('/questions', methods=['POST'])
def create_question():
    """Method for Creating a new question"""
    

    data = request.get_json()

    questionId = data["questionId"]
    createdOn = data["createdOn"]
    createdBy = ["createdBy"]
    meetup = ["meetup"]
    title =   ["title"]
    body =   ["body"]
    votes = ["votes"]
    
    questions.add_question(questionId, createdOn, createdBy, meetup, title, body, votes)

    return make_response(jsonify({

        "data" : {                
            "questionId": questionId,
            "createdOn": createdOn,
            "createdBy": createdBy,
            "meetup": meetup,
            "title":   title,
            "body":   body,
            "votes": votes,
        },
            "status": 201
        }), 201)
        # .....................................
@question_version1.route('/questions', methods=['GET'])
def retrieve_questions():
    """Return all questions"""
    all_questions = questions.get_all_questions()
    return make_response(jsonify({
            "All questions": all_questions
        }), 200)



