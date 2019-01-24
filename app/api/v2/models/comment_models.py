"""Comments model"""
from instance.db_con import con_return

comments = []


class CommentModels():
    """The Comments Model Class"""

    def __init__(self):
        """Initializing the User Model Class"""
        self.con = con_return()
        self.cur = self.con.cursor()

    def add_comment(self, questionId, title, body, comment):
        """Adding New comment"""
        payload = {
            "questionId": questionId,
            "title":   title,
            "body":   body,
            "comment": comment
        }

        self.cur.execute(
            "INSERT INTO comments(questionId, title, body, comment) VALUES(%s, %s, %s, %s)",
            (questionId,
             title,
             body,
             comment))

        self.con.commit()
        self.con.close()

        return payload

    def get_all_comments(self):
        """Return all questions"""
        self.cur.execute("SELECT * FROM comments")
        data = self.cur.fetchall()

        all_comments = []
        for item in data:
            print(item)

            payload = {
                "Comment Id": item[0],
                "Question Id": item[1],
                "Title": item[2],
                "Body": item[3],
                "Comment": item[4]
            }
            all_comments.append(payload)

        return all_comments

    def get_one_comment(self, questionId):
        """Fetch specific question's comments"""
        for comment in comments:
                if int(questionId) == comment['questionId']:
                    return comment

        # return fetch_one_comment(comments, questionId)

    def write_comment(self, comment_data):
        """Return specific comments"""
        return comment_data
