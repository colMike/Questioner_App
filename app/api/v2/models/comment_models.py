"""Comments model"""

from app.api.v2.utils.manage import fetch_one_comment
from instance.db_con import cur, con

comments = []


class CommentModels:
    """The Comments Model Class"""

    def __init__(self):
        """Initializing the Comments Model Class"""
        pass

    def add_comment(self, questionId, title, body, comment):
        """Adding New comment"""
        payload = {
            "questionId": questionId,
            "title":   title,
            "body":   body,
            "comment": comment
        }

        cur.execute(
            "INSERT INTO comments(questionId, title, body, comment) VALUES(%s, %s, %s, %s)",
            (questionId,
             title,
             body,
             comment))

        con.commit()

        return payload

    def get_all_comments(self):
        """Return all questions"""
        return comments

    def get_one_comment(self, questionId):
        """Return specific comments"""
        return fetch_one_comment(comments, questionId)

    def write_comment(self, comment_data):
        """Return specific comments"""
        return comment_data
