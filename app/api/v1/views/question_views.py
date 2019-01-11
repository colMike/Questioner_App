"""question views File"""
from app.api.v1.models.question_models import QuestionModels
from flask import Blueprint, make_response, jsonify, request

question_version1 = Blueprint(
    'question_version1', __name__, url_prefix='/api/v1')
questions = QuestionModels()


@question_version1.route('/questions', methods=['POST'])
def create_question():
    """Method for Creating a new question"""

    data = request.get_json()

    questionId = data["questionId"]
    createdOn = data["createdOn"]
    createdBy = ["createdBy"]
    meetup = ["meetup"]
    title = ["title"]
    body = ["body"]
    votes = ["votes"]

    questions.add_question(questionId, createdOn,
                           createdBy, meetup, title, body, votes)

    return make_response(jsonify({

        "data": {
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


@question_version1.route('/questions', methods=['GET'])
def retrieve_questions():
    """Return all questions"""
    all_questions = questions.get_all_questions()
    return make_response(jsonify({
        "All questions": all_questions
    }), 200)


@question_version1.route('/questions/<questionId>', methods=['GET'])
def retrieve_one_question(questionId):
    """Return one question"""
    one_question = questions.get_one_question(questionId)
    return make_response(jsonify({
        "status":200, "data": one_question
        }), 200)


@question_version1.route('/questions/<questionId>/upvote', methods=['PATCH'])
def upvote_question(questionId):
    """
    The upvote question route endpoint
    """
    one_question = questions.get_one_question(questionId)
    # if one_question:
    #     question = one_question[0]
    #     question['votes'] = question['votes'] + 1
    #     return jsonify({"status": 200, "data": question}), 200
    # return jsonify({"status": 404, "error": "Question not found"}), 404
    question = [
        {
            "questionId": 1,
            "createdOn": "15th Jan 2014",
            "createdBy": 5,
            "question": 18,
            "title":   "Andela Bootcamp",
            "body":   "This is an Andela bootcamp meeting",
            "votes": 24
        }
    ]
    question[0]['votes'] = (question[0]['votes'] + 1)
    return jsonify({"status": 200, "data": question[0]}), 200

@question_version1.route("/questions/<int:questionId>/downvote", methods=['PATCH'])
def downvote_question(questionId):
    """
    The downvote question route endpoint
    """
    one_question = questions.get_one_question(questionId)
    question = [
        {
            "questionId": 1,
            "createdOn": "15th Jan 2014",
            "createdBy": 5,
            "question": 18,
            "title":   "Andela Bootcamp",
            "body":   "This is an Andela bootcamp meeting",
            "votes": 24
        }
    ]
    question[0]['votes'] = (question[0]['votes'] - 1)
    return jsonify({"status": 200, "data": question[0]}), 200

