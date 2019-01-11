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
            "body":   "This is an Andela bootcamp meeting",
            "votes": 24,
        }

        

    def test_create_question(self):
        """Test for creating a new question"""
        response = self.app.post('api/v1/questions',
                                 data=json.dumps(self.data),
                                 content_type="application/json")

        # result = json.loads(response.data)

        # self.assertEqual(result["title"], "Andela Bootcamp")
        self.assertEqual(response.status_code, 201)

    def test_retrieve_questions(self):
            """Test for retrieving all questions"""
            response = self.app.get('api/v1/questions',
                                    data=json.dumps(self.data),
                                    content_type="application/json")

            self.assertEqual(response.status_code, 200)

    def tearDown(self):
        """ Destroys set up data before running each test """
        self.app = None


if __name__ == "__main__":
    unittest.main()