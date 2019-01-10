"""User models"""
from app.api.v1.utils.manage import find_username, find_password

users = [{
    "firstname": "Mike",
	"lastname": "Mbugua",
	"othername": "Sam",
    "email": "abc.com",
    "phoneNumber": "123456",
    "username": "colmic76",
    "registered": "registered",
    "isAdmin": "False",
    "password": "colmic76"
}]


class UserModels:
    """The user Models Class"""
    def __init__(self):
        """Initializing the User Model Class"""
        pass
    
    def add_user(self, firstname, lastname, othername, email, phoneNumber, username, registered, isAdmin, password):
        """Adding New Users"""
        user_data = {
                "id": len(users) + 1,
                "firstname": firstname,
                "lastname": lastname,
                "othername": othername,
                "email": email,
                "phoneNumber": phoneNumber,
                "username": username,
                "registered": registered,
                "isAdmin": False,
                "password": password
        }
        user_info = users.append(user_data)
        return user_info
    

    def find_by_username(self, username):
        """Find a user by username"""
        return find_username(users, username)

    def check_password(self, password):
        """Check if password matches"""
        return find_password(users, password)
        

   
        
    
    
    

    