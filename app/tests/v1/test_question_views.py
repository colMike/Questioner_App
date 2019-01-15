"""This module tests the questions endpoints"""
import json
import unittest
from ... import create_app


class TestquestionEndPoints(unittest.TestCase):
    """Class that handles All test cases for questions endpoints"""

    def setUp(self):
        """Code to be excecuted before each test"""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app
        self.app.testing = True

        self.data = {
	            "createdBy": "Michael Mbugua",
                "meetup": 1,
                "title":   "Bourne Legacy",
                "body":   "So how often will we have to meet?",
                "votes": 5
            }

    def test_add_question(self):
        """Test for creating a new question"""
        response = self.client.post('api/v1/questions',
                                 data=json.dumps(self.data),
                                 content_type="application/json")

        self.assertEqual(response.status_code, 201)

    def test_get_all_questions(self):
            """Test for retrieving all questions"""
            response = self.client.get('api/v1/questions',
                                    data=json.dumps(self.data),
                                    content_type="application/json")

            self.assertEqual(response.status_code, 200)

    def test_get_one_question(self):
            """Test for retrieving all questions"""
            response = self.client.get('api/v1/questions/1',
                                    data=json.dumps(self.data),
                                    content_type="application/json")

            self.assertEqual(response.status_code, 201)

    def test_upvote(self):
            """Test for retrieving all questions"""
            response = self.client.patch('api/v1/questions/1',
                                      data=json.dumps(self.data),
                                      content_type="application/json")

            self.assertEqual(response.status_code, 404)

    def test_downvote(self):
        """Test for retrieving all questions"""
        response = self.client.patch('api/v1/questions/1',
                                  data=json.dumps(self.data),
                                  content_type="application/json")
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        """ Destroys set up data before running each test """
        self.app = None


if __name__ == "__main__":
    unittest.main()
