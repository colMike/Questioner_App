"""question models"""
import datetime
from instance.db_con import con_return


questions = []


class QuestionModels:
    """The question Models Class"""

    def __init__(self):
        """Initializing the User Model Class"""
        self.con = con_return()
        self.cur = self.con.cursor()

    def add_question(self, createdBy, meetup, title, body):
        """Adding New questions"""

        query = "INSERT INTO questions(createdBy, meetup, title, body, votes) VALUES('{}', '{}', '{}', '{}', '{}')".format(
            createdBy, meetup, title, body, 0)

        self.cur.execute(query)
        self.con.commit()

        query = "SELECT * FROM questions WHERE title= '{}';".format(title)
        self.cur.execute(query)

        data = self.cur.fetchone()
        print(data)

        record = {
            "questionId": data[0],
            "Created On": data[1],
            "Created By": data[2],
            "Meetup": data[3],
            "Title": data[4],
            "Body": data[5],
            "Votes": data[6]
        }

        return record

    def get_all_questions(self):
        """Return all questions"""
        self.cur.execute("SELECT * FROM questions")
        data = self.cur.fetchall()

        all_questions = []
        for item in data:

            print(item)

            payload = {
                "questionId": item[0],
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
        query = "SELECT * FROM questions WHERE questionId= '{}';".format(
            questionId)
        self.cur.execute(query)

        data = self.cur.fetchone()
        

        if data:
             return data
        else:
             return None

    def upvote(self, questionId):
        """Method to upvote a question"""

        query = "SELECT * FROM questions WHERE questionId= '{}';".format(
            questionId)
        self.cur.execute(query)
        data = self.cur.fetchone()

        if data:
            question = data

        else:
            return None

        current_vote = int(question[6]) + 1

        self.cur.execute("UPDATE questions SET votes = '{}' WHERE questionId = '{}';".format(
            current_vote, questionId))
        self.con.commit()
        self.cur.execute(
            "SELECT * FROM questions WHERE questionId= '{}';".format(questionId))

        data = self.cur.fetchone()

        result = {
            "QuestionId": data[0],
            "Votes": data[6]
        }

        return result

    def downvote(self, questionId):
        """Method to downvote a question"""

        query = "SELECT * FROM questions WHERE questionId= '{}';".format(
            questionId)
        self.cur.execute(query)
        data = self.cur.fetchone()

        if data:
            question = data

        else:
            return None

        if question[6] > 0:
            current_vote = int(question[6]) - 1

            self.cur.execute("UPDATE questions SET votes = '{}' WHERE questionId = '{}';".format(
                current_vote, questionId))
            self.con.commit()

            self.cur.execute(
                "SELECT * FROM questions WHERE questionId= '{}';".format(questionId))

            data = self.cur.fetchone()

            result = {
                "QuestionId": data[0],
                "Votes": data[6]
            }

            return result
