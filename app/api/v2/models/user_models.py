"""User models"""
from app.api.v2.utils.manage import find_username, find_password, user_exists
from instance.db_con import cur, con


class UserModels:
    """The user Models Class"""

    def __init__(self):
        """Initializing the User Model Class"""
        pass

    def add_user(self, firstname, lastname, othername, email, phoneNumber, username, password):
        """Adding New Users"""

        payload = {
            "Username": username,
            "email": email,
            "PhoneNumber": phoneNumber
        }
        cur.execute(
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

        con.commit()

        return payload

    def find_by_username(self, username):
        """Find a user by username"""
        return find_username(username)

    def check_password(self, username, password):
        """Check if password matches"""
        return find_password(username, password)

    def check_exists(self, username, email):
        """"Check if a user already exists"""
        return user_exists(username, email)

    def get_all_users(self):
        """Return all users in the database"""
        cur.execute("SELECT * FROM users")
        data = cur.fetchall()

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
