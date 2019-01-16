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

        self.meetup = {
            "location": 'Taj Mall, Nairobi',
            "images": ["Food.jpg", "Kitchen.jpg"],
            "topic": 'Making Pasta',
            "happeningOn":  '2nd Jan 2019, 09:40AM',
            "tags":  ["Art", "Homestudy"]
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

        res = self.app.post('/api/v1/meetups', json=self.meetup,
                            headers={'Content-Type': 'application/json'})
        data = res.get_json()

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data["status"], 201)
        self.assertEqual(data["message"], 'Meetup Added Successfully')

    # def post_rsvp(self, path="api/v1/meetups/1/rsvps", data={"reply": "no"}):
    #        """ Creates a meetup """
    #        data = self.post_data

    #        response = self.app.post(path, data=json.dumps(
    #            data), content_type="application/json")

    #        return response

    def test_post_rsvp(self):
        """Test for posting RSVP for a meetup"""
        # Create meetup first
        self.app.post('/api/v1/meetups', json=self.meetup,
                            headers={'Content-Type': 'application/json'})
        

        res = self.app.post('/api/v1/meetups/1/rsvps')
        data = res.get_json()

        print("**************")
        print(res)
        print(data['data'])
        print(len(data['data']))         
        print("**************")

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)


#         response = self.app.get('api/v1/meetups/1')
# # 
#         self.assertEqual(response.status_code, 200)
        
    #     new_rsvp = self.post_rsvp("yes")

    #     self.assertEqual(new_rsvp.status_code, 404)

    # -------------------------------------------------
    def test_retrieve_meetups(self):
        """ Test fetch all upcoming meetups """
        
        self.app.post('/api/v1/meetups', json=self.meetup,
                            headers={'Content-Type': 'application/json'})
        self.app.post('/api/v1/meetups', json=self.meetup,
                            headers={'Content-Type': 'application/json'})

              
        # print("**************")
        # print(res)
        # print(data['data'])
        # print(len(data['data']))         
        # print("**************")


        res_two = self.app.get('/api/v1/meetups/upcoming')
        data_two = res_two.get_json()


        self.assertEqual(res_two.status_code, 200)
        self.assertEqual(data_two['status'], 200)
        self.assertEqual(len(data_two['data']), 4)
    # -------------------------------------------------

    def test_retrieve_one_meetup(self):

        """Test for retrieving all meetups"""



        self.app.post('/api/v1/meetups', json=self.meetup,
                            headers={'Content-Type': 'application/json'})
        self.app.post('/api/v1/meetups', json=self.meetup,
                            headers={'Content-Type': 'application/json'})

              

        res = self.app.get('/api/v1/meetups/1')
        data = res.get_json()

        # print("**************")
        # print(res)
        # print(data['data'])
        # print(len(data['data']))         
        # print("**************")

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)


        response = self.app.get('api/v1/meetups/1')
# 
        self.assertEqual(response.status_code, 200)

    
    
    def tearDown(self):
        """ Destroys set up data before running each test """
        self.app = None


if __name__ == "__main__":
    unittest.main()
