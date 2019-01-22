"""User models"""
# from app.api.v2.utils.manage import find_username, find_password, user_exists
from instance.db_con import con_return

class UserModels:
    """The user Models Class"""

    def __init__(self):
        """Initializing the User Model Class"""
        self.con=con_return()
        self.cur=self.con.cursor()

    def add_user(self, firstname, lastname, othername, email, phoneNumber, username, password):
        """Adding New Users"""

        payload = {
            "Username": username,
            "email": email,
            "PhoneNumber": phoneNumber
        }
        self.cur.execute(
            "INSERT INTO users(firstname, lastname, othername, email, phoneNumber, username, registered, isAdmin, password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (firstname,
             lastname,
             othername,
             email,
             phoneNumber,
             username,
             True,
             False,
             password))

        self.con.commit()
        self.cur.execute("SELECT * FROM users WHERE username= %s",
                        (username,))

        data = self.cur.fetchone()

        payload = {
            "Firstname": data[1],
            "Lastname": data[2],
            "Othername": data[3],
            "email": data[4],
            "phoneNumber": data[5],
            "username": data[6]
        }

        return payload

    def find_by_username(self, username):
        """Find a user by username"""
        
        self.cur.execute(
        "SELECT * FROM users WHERE username= %s", (username))

        username_data = self.cur.fetchone()

        if username_data:
            return True
        else:
            return False
        
        
    def check_password(self, username, password):
        """Check if password matches"""
        
        """Look if the password matches the one in the database"""
        self.cur.execute(
            "SELECT * FROM users WHERE username= %s", (username))

        data = self.cur.fetchone()

        if data == None:
            pass
        else:
            """Get password from database"""
            pass_in_db = data[9]
            if pass_in_db == password:
                return data
            else:
                return None 

        
        

    def check_exists(self, username, email):
        """"Check if a user already exists"""

        self.cur.execute(
        "SELECT * FROM users WHERE username= %s OR email = %s", (username, email))

        data = self.cur.fetchall()

        if data:
            return True

        else:
            return False    


    def get_all_users(self):
        """Return all users in the database"""
        self.cur.execute("SELECT * FROM users")
        data = self.cur.fetchall()

        all_users = []
        for item in data:

            payload = {
                "firstname": item[1],
                "lastname": item[2],
                "othername": item[3],
                "email": item[4],
                "phoneNumber": item[5],
                "username": item[6],
                "Registered": item[7],
                "isAdmin": item[8],
                "Password": item[9]
            }
            all_users.append(payload)

        return all_users
