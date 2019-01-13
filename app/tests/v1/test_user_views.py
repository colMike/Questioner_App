"""This module tests endpoint"""
import json
import unittest
from ... import create_app

class TestUserEndPoint(unittest.TestCase):
    """Class that handles User Authentication endpoint tests"""
    
    def setUp(self):
        """Code to be excecuted before each test"""
        self.app = create_app()
        self.app.testing = True
        self.app = self.app.test_client()
       
        self.data = {
	        "firstname": "Mike",
	        "lastname": "Mbugua",
	        "othername": "Sam",
            "email": "abc.com",
            "phoneNumber": "123456",
            "username": "colmic76",
            "registered": "registered",
            "isAdmin": "False",
            "password": "colmic76"
        }

    def test_signup(self):
        """Test for user registration"""

        response = self.app.post('api/v1/auth/signup',
                                data = json.dumps(self.data), 
                                content_type="application/json")

        result = json.loads(response.data)
        
        self.assertEqual(result["firstname"], "Mike")
        self.assertEqual(result["lastname"], "Mbugua")
        self.assertEqual(result["othername"], "Sam")
        self.assertEqual(result["email"], "abc.com")
        self.assertEqual(result["phoneNumber"], "123456")
        self.assertEqual(result["username"], "colmic76")
        self.assertEqual(result["isAdmin"], "False")

        self.assertEqual(response.status_code, 201)



    def test_login(self):
        """Test for the user login endpoint"""

        response = self.app.post('api/v1/auth/login',
                                data = json.dumps(self.data), 
                                content_type="application/json")

        result = json.loads(response.data)
        
        self.assertEqual(result["username"], "colmic76")
        self.assertEqual(result["password"], "colmic76")

        self.assertEqual(response.status_code, 201)

    def tearDown(self):
        """ Destroys set up data before running each test """
        self.app = None


if __name__ == "__main__":
    unittest.main()
