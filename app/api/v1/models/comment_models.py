"""Comments model"""

from app.api.v1.utils.manage import fetch_one_comment

comments = [{
    "questionId": 1,
    "title":   "Andela Bootcamp",
    "body":   "This is an Andela bootcamp meeting",
    "comment": "I like your Question",
        
}]



class CommentModels:
    """The Comments Model Class"""
    def __init__(self):
        """Initializing the Comments Model Class"""
        pass
    
    def add_comment(self, title, body, comment):
        """Adding New questions"""
        comment_data = {
                "questionId": len(comments) + 1,   
                "title":   title,
                "body":   body,
                "comment": comment

        }

        
        comments.append(comment_data)
        return comments
    

    def get_all_comments(self):
        """Return all questions"""
        return comments

    def get_one_comment(self, questionId):
        """Return specific comments"""
        return fetch_one_comment(comments, questionId)

    