"""question models"""

from app.api.v1.utils.manage import fetch_one_question

questions = []



class QuestionsModel():
    """The question Models Class"""
    def __init__(self):
        """Initializing the question Model Class"""
        self.db = questions
    
    def add_question(self, createdOn, createdBy, meetup, title, body, votes):
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
        self.db.append(question_data)

        return self.db
    

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
                question["votes"] = current_vote - 1 
                return question

             