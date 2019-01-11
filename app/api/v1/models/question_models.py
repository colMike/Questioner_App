"""question models"""
from app.api.v1.utils.manage import fetch_question

questions = [{
    "questionId": 1,
    "createdOn": "15th Jan 2014",
    "createdBy": 5,
    "meetup": 18,
    "title":   "Andela Bootcamp",
    "body":   "This is an Andela bootcamp meeting",
    "votes": 24
        
}]



class QuestionModels:
    """The question Models Class"""
    def __init__(self):
        """Initializing the question Model Class"""
        pass
    
    def add_question(self, questionId, createdOn, createdBy, meetup, title, body, votes):
        """Adding New questions"""
        question_data = {
                "questionId": len(questions) + 1,   
                "createdOn": createdOn,
                "createdBy": createdBy,
                "meetup": meetup,
                "title":   title,
                "body":   body,
                "votes": votes

        }
        question_info = questions.append(question_data)
        return question_info
    

    def get_all_questions(self):
        """Return all questions"""
        return questions

    def get_one_question(self, questionId):
        """Return specific questions"""
        return fetch_question(questions, questionId)

    