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
            "password": "colmic76"
        }

    
    def test_signup(self):
        """ Test sign up with correct data """
        user = {
            'firstname': 'Michael',
            'lastname': 'Mbugua',
            'othername': 'Colmike',
            'username': 'SirMike',
            'email': 'mike@gmail.com',
            'password': 'mikemike',
            'phoneNumber': '0708453910'
        }

        res = self.app.post('api/v1/auth/users/signup', json=user,
                            headers={'Content-Type': 'application/json'})
        data = res.get_json()
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'User Added Successfully')

    def test_login(self):
        """First test for successful login """

        user = {
            'firstname': 'Michael',
            'lastname': 'Mbugua',
            'othername': 'Colmike',
            'username': 'SirMikey',
            'email': 'mikey@gmail.com',
            'password': 'mikemike',
            'phoneNumber': '0708453910'
        }

        res = self.app.post('api/v1/auth/users/signup', json=user,
                            headers={'Content-Type': 'application/json'})
        data = res.get_json()

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'User Added Successfully')

        res_other = self.app.post('/api/v1/auth/users/login', json={
                                  'username': 'SirMikey', 'password': 'mikemike'}, headers={'Content-Type': 'application/json'})
        data_other = res_other.get_json()

        self.assertEqual(res_other.status_code, 201)
        self.assertEqual(data_other['status'], 201)
        self.assertEqual(data_other['message'], 'User Logged in Successfully')

        self.assertEqual(res_other.status_code, 201)
        self.assertEqual(data_other['Status'], 201)
        self.assertEqual(data_other['Message'], 'User Logged in Successfully')
   
    
    
    def tearDown(self):
        """ Destroys set up data before running each test """
        self.app = None


if __name__ == "__main__":
    unittest.main()
