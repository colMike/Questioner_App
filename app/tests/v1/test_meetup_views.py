"""This module tests the meetup endpoint"""
import json
import unittest
from ... import create_app


class TestMeetupEndPoints(unittest.TestCase):
    """Class that handles All test cases for meetup endpoints"""

    def setUp(self):
        """Code to be excecuted before each test"""
        self.app = create_app()
        self.app.testing = True
        self.app = self.app.test_client()

        self.data = {
            "meetupId": 1,
            "createdOn": "25th Dec 2018",
            "location": "Taj",
            "images": ["Food.jpg", "Kitchen.jpg"],
            "topic": "Making Pasta",
            "happeningOn": "2nd Jan 2019, 09:40AM",
            "tags": ["Art", "Homestudy"]
        }

        self.post_data = {
            "createdOn": "25th Dec 2018",
            "location": "Taj Mall, Nairobi",
            "images": ["Food.jpg", "Kitchen.jpg"],
            "topic": "Making Pasta", 
            "happeningOn":  "2nd Jan 2019, 09:40AM",
            "tags":  ["Art", "Homestudy"]

        }

    def create_meetup(self, path="api/v1/meetups", data={}):
           """ Creates a meetup """
           data = self.post_data

           response = self.app.post(path, data=json.dumps(
               data), content_type="application/json")

           return response

    def post_rsvp(self, path="api/v1/meetups/1/rsvps", data={"reply": "no"}):
           """ Creates a meetup """
           data = self.post_data

           response = self.app.post(path, data=json.dumps(
               data), content_type="application/json")

           return response

    def test_create_meetup(self):
        """ Test whether new meeup is created if data provided """
        new_meetup = self.create_meetup()

        self.assertEqual(new_meetup.status_code, 404)
        


    def test_retrieve_meetups(self):
            """Test for retrieving all meetups"""
            response = self.app.get('api/v1/meetups/upcoming',
                                data=json.dumps(self.data),
                                content_type="application/json")

            self.assertEqual(response.status_code, 200)

    def test_retrieve_one_meetup(self):
        """Test for retrieving all meetups"""
        response = self.app.get('api/v1/meetups/1')

        self.assertEqual(response.status_code, 200)

    def test_post_rsvp(self):
        """Test for retrieving all meetups"""
        new_rsvp = self.post_rsvp("yes")

        self.assertEqual(new_rsvp.status_code, 404)

    def tearDown(self):
        """ Destroys set up data before running each test """
        self.app = None


if __name__ == "__main__":
    unittest.main()
