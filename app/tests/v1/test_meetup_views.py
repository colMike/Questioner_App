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


    def test_create_meetup(self):
        """Test for creating a new meetup"""
        response = self.app.post('api/v1/meetups',
                                data = json.dumps(self.data), 
                                content_type="application/json")
        
    
        
        self.assertEqual(response.status_code, 201)


    def test_retrieve_meetups(self):
            """Test for retrieving all meetups"""
            response = self.app.get('api/v1/meetups',
                                    data = json.dumps(self.data), 
                                    content_type="application/json")

            
            self.assertEqual(response.status_code, 200)
    
    def test_retrieve_one_meetup(self):
        """Test for retrieving all meetups"""
        response = self.app.get('api/v1/meetups/1',
                                data = json.dumps(self.data), 
                                content_type="application/json")
        
        self.assertEqual(response.status_code, 200)
    

    def tearDown(self):
        """ Destroys set up data before running each test """
        self.app = None


if __name__ == "__main__":
    unittest.main()
 

