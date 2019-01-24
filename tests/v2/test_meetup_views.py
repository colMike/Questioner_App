"""This module tests endpoint"""
import json
import unittest
from app import create_app
from flask_jwt_extended import (create_access_token)
from instance.db_con import con_return, destroy_tables, create_tables

class TestMeetupEndPoints(unittest.TestCase):
    """Class that handles All test cases for meetup endpoints"""

    def setUp(self):
        """Code to be excecuted before each test"""
        self.app = create_app(config_name="testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        self.meetup = {
    
            "location": "Taj Mall, Nairobi",
            "meetup_images": ["Food.jpg", "Kitchen.jpg"],
            "happeningOn":  "2nd Jan 2019, 09:40AM",
            "meetup_tags":  ["Art", "Homestudy"],
            "topic": "Appreciating Culture"
        }

        self.post_data = {
            "location": "Taj",
            "images": ["Food.jpg", "Kitchen.jpg"],
            "topic": "Making Pasta",
            "happeningOn": "2nd Jan 2019, 09:40AM",
            "tags": ["Art", "Homestudy"]
        }

    def test_create_meetup(self):
        """ Test whether new meetup is created if data provided """

        token = create_access_token(identity="admin")

        res = self.client.post('api/v2/meetups',json=self.meetup,
                        headers={'Content-Type': 'application/json' , 'Authorization': 'Bearer {}'.format(token)})
        

        data = res.get_json()
        

        self.assertEqual(res.status_code, 201)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data["status"], 201)
        self.assertEqual(data["message"], 'Meetup Added Successfully')

    def test_retrieve_meetups(self):
        """ Test fetch all upcoming meetups """
        token = create_access_token(identity="admin")
        self.client.post('/api/v2/meetups', json=self.meetup,
                      headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})
        self.client.post('/api/v2/meetups', json=self.meetup,
                      headers={'Content-Type': 'application/json' , 'Authorization': 'Bearer {}'.format(token)})

        res_two = self.client.get('/api/v2/meetups/upcoming')
        data_two = res_two.get_json()

        self.assertEqual(res_two.status_code, 200)
        self.assertEqual(data_two['status'], 200)
        self.assertEqual(len(data_two['data']), 2)

    def test_retrieve_one_meetup(self):
        """Test for retrieving one meetup"""
        token = create_access_token(identity="admin")

        res = self.client.post('/api/v2/meetups', json=self.meetup,
                      headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})


        data = res.get_json()
        
        meetupId = data['data']['meetupId']
        url = 'api/v2/meetups/{}'.format(meetupId)
        res = self.client.get(url)
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)

    def test_rsvp_for_meetup(self):
        rsvp = {"reply": "yes"}
        token = create_access_token(identity="admin")

        res = res = self.client.post('/api/v2/meetups', json=self.meetup,
                      headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})
        data = res.get_json()
        
        meetupId = data['data']['meetupId']
        url = 'api/v2/meetups/{}/rsvps'.format(meetupId)

        res = self.client.post(url, json=rsvp,
                      headers={'Content-Type': 'application/json'})
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)

    def test_rsvp_meetup_noData(self):
        """Test rsvp without Reply data"""
        rsvp = {"reply": ""}
        token = create_access_token(identity="admin")
        
        res = res = self.client.post('/api/v2/meetups', json=self.meetup,
                      headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})
        data = res.get_json()
        
        meetupId = data['data']['meetupId']
        url = 'api/v2/meetups/{}/rsvps'.format(meetupId)

        res = self.client.post(url, json=rsvp,
                      headers={'Content-Type': 'application/json'})
        data = res.get_json()

        self.assertEqual(res.status_code, 400)

    def test_delete_meetup(self):
        """Test Delete a meetup"""
        meetup = {
            "location": "Kisumu",
            "meetup_images": ["Driver.jpg", "Landscape.jpg"],
            "topic": "Vehicle Mechanics",
            "happeningOn": "2nd Jan 2019, 09:40AM",
            "meetup_tags": ["Art", "Homestudy"]
        }
        
        token = create_access_token(identity="admin")

        res = self.client.post('api/v2/meetups',json=meetup,
                        headers={'Content-Type': 'application/json' , 'Authorization': 'Bearer {}'.format(token)})
       
        data = res.get_json()


        meetupId = data['data']['meetupId']
        url = 'api/v2/meetups/{}'.format(meetupId)

        res = self.client.delete(url,
                            headers={'Content-Type': 'application/json' , 'Authorization': 'Bearer {}'.format(token)})

        print(res)
        data = res.get_json()
    
        self.assertEqual(res.status_code, 200)

        


    def tearDown(self):
        """ Destroys set up data before running each test """
        self.app = None
        destroy_tables()


if __name__ == "__main__":
    unittest.main()
