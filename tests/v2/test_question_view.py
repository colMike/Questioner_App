"""This module tests endpoint"""
import json
import unittest
from app import create_app
from instance.db_con import con_return, destroy_tables, create_tables

class TestquestionEndPoints(unittest.TestCase):
    """Class that handles All test cases for questions endpoints"""

    def setUp(self):
        """Code to be excecuted before each test"""
        self.app = create_app(config_name="testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        self.data = {
            "questionId": 1,
            "createdOn": "15th Jan 2014",
            "createdBy": 5,
            "question": 18,
            "title":   "Andela Bootcamp",
            "body":   "This is an Andela bootcamp meeting",
            "votes": 24,
        }

        self.post = {
                "createdBy": 1,
                "meetup": 1,
                "title":   "Bourne Legacy",
                "body":   "So how often will we have to meet?"
            }

        self.comment = {
            "comment": "Your'e Awesome"
        } 

    def test_create_question(self):
        """Test for creating a new question"""
        response = self.client.post('api/v2/questions',
                                 data=json.dumps(self.post),
                                 content_type="application/json")

        self.assertEqual(response.status_code, 201)

    def test_create_question_no_Title(self):
        """Test for creating a new without a title"""
        post_data = {
            "createdBy": 1,
            "meetup": 1,
            "title":   None,
            "body":   "So how often will we have to meet?",
            "votes": 5

        }

        response = self.client.post('api/v2/questions',
                                 data=json.dumps(post_data),
                                 content_type="application/json")
        
        data = response.get_json()
        self.assertEqual(data['message'], "Invalid data. Please fill all required fields")
        self.assertEqual(response.status_code, 400)


    def test_retrieve_questions(self):
            """Test for retrieving all questions"""
            response = self.client.get('api/v2/questions')

            self.assertEqual(response.status_code, 200)

    def test_get_question(self):
        """Test for retrieving one question"""

        res = self.client.post('api/v2/questions',
                                 data=json.dumps(self.post),
                                 content_type="application/json")
        data = res.get_json()
        
        questionId = data['data']['questionId']
        
        url = 'api/v2/questions/{}'.format(questionId)

        response = self.client.get(url,
                                data=json.dumps(self.data),
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_upvote_question(self):
        """Test for Upvoting a Question"""
        res = self.client.post('api/v2/questions',
                                 data=json.dumps(self.post),
                                 content_type="application/json")
        data = res.get_json()
        
        questionId = data['data']['questionId']
        
        url = 'api/v2/questions/{}/upvote'.format(questionId)

        response = self.client.patch(url,
                                  data=json.dumps(self.data),
                                  content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_downvote_question(self):
        """Test for Downvoting a Question"""
        res = self.client.post('api/v2/questions',
                                 data=json.dumps(self.post),
                                 content_type="application/json")
        data = res.get_json()
        
        questionId = data['data']['questionId']
        
        url1 = 'api/v2/questions/{}/upvote'.format(questionId)
        url2 = 'api/v2/questions/{}/downvote'.format(questionId)

        response = self.client.patch(url1,
                                  data=json.dumps(self.data),
                                  content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response = self.client.patch(url2,
                                  data=json.dumps(self.data),
                                  content_type="application/json")
        self.assertEqual(response.status_code, 200)



    def test_comment_on_question(self):
        """Test if a user can add a comment to a question"""

        """Set up a dummy Question"""
        res = self.client.post('api/v2/questions',
                                 data=json.dumps(self.post),
                                 content_type="application/json")


        data = res.get_json()
        
        questionId = data['data']['questionId']
        
        url = 'api/v2/{}/comments'.format(questionId)

        response = self.client.post(url,
                                 data=json.dumps(self.comment),
                                 content_type="application/json")

        self.assertEqual(response.status_code, 200)        

    def test_empty_comment_on_question(self):
        """Test if an empty comment work on a question"""

        res = self.client.post('api/v2/questions',
                                 data=json.dumps(self.post),
                                 content_type="application/json")

        data = res.get_json()
        
        questionId = data['data']['questionId']
        
        url = 'api/v2/{}/comments'.format(questionId)

        response = self.client.post(url,
                                 json = {},
                                 content_type="application/json")

        self.assertEqual(response.status_code, 400)                   


    def tearDown(self):
        """ Destroys set up data before running each test """
        self.app = None
        destroy_tables()


if __name__ == "__main__":
    unittest.main()
    