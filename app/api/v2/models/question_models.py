"""question models"""
import datetime
from app.api.v2.utils.manage import fetch_one_question

questions = []


class QuestionModels:
    """The question Models Class"""

    def __init__(self):
        """Initializing the question Model Class"""
        pass

    def add_question(self, createdBy, meetup, title, body):
        """Adding New questions"""
        question_data = {
            "questionId": len(questions) + 1,
            "createdOn": datetime.datetime.now(),
            "createdBy": createdBy,
            "meetup": meetup,
            "title":   title,
            "body":   body,
            "votes": 0

        }

        questions.append(question_data)
        return questions

    def get_all_questions(self):
        """Return all questions"""
        return questions

    def get_one_question(self, questionId):
        """Return specific questions"""
        return fetch_one_question(questions, questionId)

    def upvote(self, questionId):
        """Method to upvote a question"""

        for question in questions:
            if int(questionId) == question['questionId']:
                current_vote = int(question["votes"])
                question["votes"] = current_vote + 1
                return question
            

    def downvote(self, questionId):
        """Method to downvote a question"""

        for question in questions:
            if int(questionId) == question['questionId']:
                current_vote = int(question["votes"])
                if current_vote >0:
                    question["votes"] = current_vote - 1
                    return question
                
