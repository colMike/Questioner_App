"""This module tests the questions endpoints"""
import json
import unittest
from ... import create_app


class TestquestionEndPoints(unittest.TestCase):
    """Class that handles All test cases for questions endpoints"""

    def setUp(self):
        """Code to be excecuted before each test"""
        self.app = create_app()
        self.app.testing = True
        self.app = self.app.test_client()

        self.data = {
            "questionId": 1,
            "createdOn": "15th Jan 2014",
            "createdBy": 5,
            "question": 18,
            "title":   "Andela Bootcamp",
            "body":   "This is an Andela bootcamp meeting"

        }

        self.post = {
            "createdBy": 1,
            "meetup": 1,
            "title":   "Bourne Legacy",
            "body":   "So how often will we have to meet?",


        }

        self.comment = {
            "comment": "Your'e Awesome"
        }

    def test_create_question(self):
        """Test for creating a new question"""
        response = self.app.post('api/v1/questions',
                                 data=json.dumps(self.post),
                                 content_type="application/json")

        self.assertEqual(response.status_code, 201)

    def test_create_question_no_Title(self):
        """Test for creating a new without a title"""
        post_data = {
            "createdBy": 1,
            "meetup": 1,
            "title":   None,
            "body":   "So how often will we have to meet?"



        }

        response = self.app.post('api/v1/questions',
                                 data=json.dumps(post_data),
                                 content_type="application/json")

        data = response.get_json()
        self.assertEqual(
            data['message'], "Invalid data. Please fill all required fields")
        self.assertEqual(response.status_code, 400)

    def test_retrieve_questions(self):
            """Test for retrieving all questions"""
            response = self.app.get('api/v1/questions')

            self.assertEqual(response.status_code, 200)

    def test_get_question(self):
        """Test for retrieving one question"""
        response = self.app.get('api/v1/questions/1',
                                data=json.dumps(self.data),
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_upvote_question(self):
        """Test for Upvoting a Question"""
        self.app.post('api/v1/questions', data=json.dumps(self.post),
                      content_type="application/json")

        response = self.app.patch('api/v1/questions/1/upvote',
                                  data=json.dumps(self.data),
                                  content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_downvote_question(self):
        """Test for Downvoting a Question"""

        self.app.post('api/v1/questions', data=json.dumps(self.post),
                      content_type="application/json")

        """Make 2 upvotes"""
        self.app.patch('api/v1/questions/1/upvote')
        self.app.patch('api/v1/questions/1/upvote')

        response = self.app.patch('api/v1/questions/1/downvote')

        self.assertEqual(response.status_code, 200)

    def test_comment_on_question(self):
        """Test if a user can add a comment to a question"""

        """Set up a dummy question"""
        self.app.post('api/v1/questions',
                      data=json.dumps(self.post),
                      content_type="application/json")

        response = self.app.post('api/v1/1/comments',
                                 data=json.dumps(self.comment),
                                 content_type="application/json")

        print(response)

        self.assertEqual(response.status_code, 200)

    def test_empty_comment_on_question(self):
        """Test if an empty comment work on a question"""
        response = self.app.post('api/v1/1/comments',
                                 json={},
                                 content_type="application/json")

        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        """ Destroys set up data before running each test """
        self.app = None


if __name__ == "__main__":
    unittest.main()


