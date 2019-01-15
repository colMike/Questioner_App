"""This module tests the meetup endpoint"""
from flask import json
import unittest
from ... import create_app


class TestMeetupEndPoints(unittest.TestCase):
    """Class that handles All test cases for meetup endpoints"""

    def setUp(self):
        """Code to be excecuted before each test"""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app
        self.app.testing = True

        self.data = {
                "createdOn": "25th Dec 2018",
                "location": "Taj Mall, Nairobi",
                "images": ["Food.jpg", "Kitchen.jpg"],
                "topic": "Making Pasta", 
                "happeningOn":  "2nd Jan 2019, 09:40AM",
                "tags":  ["Art", "Homestudy"]
        }


    def test_add_meetup(self):
        """Test for creating a new question"""
        response = self.client.post('api/v1/meetups',
                                 data=json.dumps(self.data),
                                 content_type="application/json")

        self.assertEqual(response.status_code, 201)

    def test_get_all_meetups(self):
            """Test for retrieving all meetup"""
            response = self.client.get('api/v1/meetup')

            self.assertEqual(response.status_code, 200)

    def test_get_one_meetup(self):
            """Test for retrieving all meetup"""
            response = self.client.get('api/v1/meetups')

            self.assertEqual(response.status_code, 201)


    def tearDown(self):
        """ Destroys set up data before running each test """
        self.app = None


if __name__ == "__main__":
    unittest.main()

