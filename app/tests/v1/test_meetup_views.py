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
            "createdOn": "25th Dec 2018",
            "location": "Taj Mall, Nairobi",
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

        result = json.loads(response.data)
        
        self.assertEqual(result["createdOn"], "25th Dec 2018")
        self.assertEqual(result["location"], "Taj Mall, Nairobi")
        self.assertEqual(result["images"], ["Food.jpg", "Kitchen.jpg"])
        self.assertEqual(result["topic"], "Making Pasta")
        self.assertEqual(result["happeningOn"], "2nd Jan 2019, 09:40AM")
        self.assertEqual(result["tags"], ["Art", "Homestudy"])

        self.assertEqual(response.status_code, 201)

    def tearDown(self):
        """ Destroys set up data before running each test """
        self.app = None


if __name__ == "__main__":
    unittest.main()
