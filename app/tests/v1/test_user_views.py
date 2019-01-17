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



        self.user = {
            'firstname': 'Michael',
            'lastname': 'Mbugua',
            'othername': 'Colmike',
            'username': 'SirMike',
            'email': 'mike@gmail.com',
            'password': 'mikemike',
            'phoneNumber': '0708453910'
        }

    def test_signup(self):
        """ Test sign up with correct data """
        user = {
            'firstname': 'Sam',
            'lastname': 'Ongeri',
            'othername': 'SamOngeri',
            'username': 'SamSmith',
            'email': 'sammy@gmail.com',
            'password': 'MrSam',
            'phoneNumber': '0708453950'
        }

        res = self.app.post('api/v1/auth/signup', json=user,
                            headers={'Content-Type': 'application/json'})
        data = res.get_json()
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'User Added Successfully')

    def test_repeat_signup(self):
        """ Test sign up with correct data """

        res = self.app.post('api/v1/auth/signup', json=self.user,
                            headers={'Content-Type': 'application/json'})
        data = res.get_json()
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['status'], 403)
        self.assertEqual(data['message'], 'User Already exists')

    def test_signup_noUsername(self):
        """Test for signup attempt without giving username"""
        user = {
            'firstname': 'Michael',
            'lastname': 'Mbugua',
            'othername': 'Colmike',
            'username': None,
            'email': 'mike@gmail.com',
            'password': 'mikemike',
            'phoneNumber': '0708453910'
        }


        res = self.app.post('api/v1/auth/signup', json=user,
                            headers={'Content-Type': 'application/json'})

        data = res.get_json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)

    def test_wrong_data_signup(self):
        """Test for signup attempt with wrong data type"""
        user = {
            'firstname': 1,
            'lastname': 'Mbugua',
            'othername': 'Colmike',
            'email': 'mike@gmail.com',
            'username': "Mikeymike",
            'password': 'mikemike',
            'phoneNumber': '0708453910'
        }

        res = self.app.post('api/v1/auth/signup', json=user,
                            headers={'Content-Type': 'application/json'})
        data = res.get_json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(
            data['message'], 'Invalid data. Please fill all required fields')

    def test_login(self):
        """First test for successful login """
        res = self.app.post('api/v1/auth/signup', json=self.user,
                            headers={'Content-Type': 'application/json'})
        data = res.get_json()

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'User Added Successfully')

        res_other = self.app.post('/api/v1/auth/login', json={
                                  'username': 'SirMike', 'password': 'mikemike'}, headers={'Content-Type': 'application/json'})
        data_other = res_other.get_json()

        self.assertEqual(res_other.status_code, 201)
        self.assertEqual(data_other['status'], 201)
        self.assertEqual(data_other['message'], 'User Logged in Successfully')

    def test_login_wrong_username(self):
        """Test login with wrong username"""
        self.app.post('api/v1/auth/signup', json=self.user,
                        headers={'Content-Type': 'application/json'})

        res_other = self.app.post('/api/v1/auth/login', json={
                                  'username': 'MrMan', 'password': 'mikemike'}, headers={'Content-Type': 'application/json'})
        data_other = res_other.get_json()

        self.assertEqual(res_other.status_code, 401)
        self.assertEqual(data_other['error'], 'User not found: Please register')

    def test_login_wrong_password(self):
        """Test login with wrong password"""
        self.app.post('api/v1/auth/signup', json=self.user,
                        headers={'Content-Type': 'application/json'})

        res_other = self.app.post('/api/v1/auth/login', json={
                                  'username': 'SirMike', 'password': '901dalmatians'}, headers={'Content-Type': 'application/json'})
        data_other = res_other.get_json()

        self.assertEqual(res_other.status_code, 401)
        self.assertEqual(data_other['error'], 'Password incorrect')

    def test_login_empty_username(self):
        """Test login with no username"""
        self.app.post('api/v1/auth/signup', json=self.user,
                        headers={'Content-Type': 'application/json'})

        res_other = self.app.post('/api/v1/auth/login', json={
                                  'username': None, 'password': 'mikemike'}, headers={'Content-Type': 'application/json'})
        data_other = res_other.get_json()

        self.assertEqual(res_other.status_code, 400)
        self.assertEqual(data_other['message'], 'Invalid data. Please fill all required fields')
    
    def test_login_empty_password(self):
        """Test login with no password"""
        self.app.post('api/v1/auth/signup', json=self.user,
                        headers={'Content-Type': 'application/json'})

        res_other = self.app.post('/api/v1/auth/login', json={
                                  'username': "SirMike", 'password': None}, headers={'Content-Type': 'application/json'})
        data_other = res_other.get_json()

        self.assertEqual(res_other.status_code, 400)
        self.assertEqual(data_other['message'], 'Invalid data. Please fill all required fields')



    def tearDown(self):
        """ Destroys set up data before running each test """
        self.app = None


if __name__ == "__main__":
    unittest.main()
