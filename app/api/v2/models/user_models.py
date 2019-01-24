"""User models"""
from instance.db_con import con_return
from werkzeug.security import generate_password_hash, check_password_hash

class UserModels:
    """The user Models Class"""

    def __init__(self):
        """Initializing the User Model Class"""
        self.con = con_return()
        self.cur = self.con.cursor()

        """Add Admin to the Database"""
        encrypted_password = generate_password_hash("admin")
        query = "INSERT INTO users (\
                    firstname, lastname, othername, email, phoneNumber, username, registered, isAdmin, password) VALUES (\
                    'admin', 'admin', 'admin', 'admin@gmail.com','0756998153', 'admin', True, True, '{}')".format(encrypted_password)

        self.cur.execute(query)
        self.con.commit()

    def add_user(self, firstname, lastname, othername, email, phoneNumber, username, password):
        """Adding New Users"""

        payload = {
            "Username": username,
            "email": email,
            "PhoneNumber": phoneNumber
        }

        encrypted_password = generate_password_hash(password)

        query = "INSERT INTO users (firstname, lastname, othername, email, phoneNumber, username, registered, isAdmin, password) VALUES ('{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}')".format(
            firstname, lastname, othername, email, phoneNumber, username, True, False, encrypted_password)

        self.cur.execute(query)

        self.con.commit()
        query = "SELECT * FROM users WHERE username= '{}';".format(username)
        self.cur.execute(query)

        data = self.cur.fetchone()

        payload = {
            "Firstname": data[1],
            "Lastname": data[2],
            "Othername": data[3],
            "email": data[4],
            "phoneNumber": data[5],
            "username": data[6],
            "password": data[9]
        }

        return payload

    def find_by_username(self, username):
        """Find a user by username"""

        self.cur.execute(
            "SELECT * FROM users WHERE username= '{}';".format(username))

        username_data = self.cur.fetchone()

        if username_data:
            return True
        else:
            return False

    def check_password(self, username, password):
        """Check if password matches"""

        """Look if the password matches the one in the database"""
        self.cur.execute(
            "SELECT * FROM users WHERE username= '{}';".format(username))

        data = self.cur.fetchone()

        if data == None:
            pass
        else:
            """Get password from database"""
            pass_in_db = data[9]
            if check_password_hash(pass_in_db, password):
            # if pass_in_db == password:
                return data
            else:
                return None

    def check_exists(self, username, email):
        """"Check if a user already exists"""

        self.cur.execute(
            "SELECT * FROM users WHERE username= '{}' OR email = '{}';".format(username, email))

        data = self.cur.fetchall()

        if data:
            return True

        else:
            return False

    def get_user(self, username):
        """Find a user by username"""

        self.cur.execute(
            "SELECT * FROM users WHERE username= '{}';".format(username))

        username_data = self.cur.fetchone()

        if username_data:
            return username_data[6]
        else:
            return None

    def get_all_users(self):
        """Return all users in the database"""
        self.cur.execute("SELECT * FROM users;")
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
