"""question models"""
import datetime
from app.api.v2.utils.manage import fetch_one_question
from instance.db_con import cur, con


questions = []


class QuestionModels:
    """The question Models Class"""

    def __init__(self):
        """Initializing the question Model Class"""
        pass

    def add_question(self, createdBy, meetup, title, body):
        """Adding New questions"""
        payload = {
            "createdOn": datetime.datetime.now(),
            "createdBy": createdBy,
            "meetup": meetup,
            "title":   title,
            "body":   body,


        }

        cur.execute(
            "INSERT INTO questions(createdBy, meetup, title, body, votes) VALUES(%s, %s, %s, %s, %s)",
            (createdBy,
             meetup,
             title,
             body,
             0))

        con.commit()

        return payload

    def get_all_questions(self):
        """Return all questions"""
        cur.execute("SELECT * FROM questions")
        data = cur.fetchall()

        all_questions = []
        for item in data:

            payload = {
                "Created On": item[1],
                "Created By": item[2],
                "Meetup": item[3],
                "Title": item[4],
                "Body": item[5],
                "Votes": item[6],
            }
            all_questions.append(payload)

        return all_questions

    def get_one_question(self, questionId):
        """Return specific questions"""
        return fetch_one_question(questionId)

    def upvote(self, questionId):
        """Method to upvote a question"""
        question = fetch_one_question(questionId)

        current_vote = int(question[6]) + 1

        cur.execute("UPDATE questions SET votes = %s WHERE questionId = %s",
                    (current_vote, questionId))
        con.commit()

        cur.execute("SELECT * FROM questions WHERE questionid= %s",
                    (questionId,))

        data = cur.fetchone()

        result = {
            "QuestionId": data[0],
            "Votes": data[6]
        }

        return result

    def downvote(self, questionId):
        """Method to downvote a question"""


        question = fetch_one_question(questionId)

        if question[6] > 0:
            current_vote = int(question[6]) - 1

            cur.execute("UPDATE questions SET votes = %s WHERE questionId = %s",
                        (current_vote, questionId))
            con.commit()

            cur.execute("SELECT * FROM questions WHERE questionid= %s",
                        (questionId,))

            data = cur.fetchone()

            result = {
                "QuestionId": data[0],
                "Votes": data[6]
            }

            return result
            