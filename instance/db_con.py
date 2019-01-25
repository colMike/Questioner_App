"""Importing flask psycopg2"""
import os
import psycopg2
from werkzeug.security import generate_password_hash

"""Create a Database Connection"""
config = os.getenv("APP_SETTINGS")

def con_return():
    """Return a connection object based on testing or development environment"""
    if config == "testing":
        db_url = os.getenv("TEST_DATABASE_URL")
        con = psycopg2.connect(db_url)
        return con

    elif config == "development":
        db_url = os.getenv("DEV_DATABASE_URL")
        con = psycopg2.connect(db_url)
        return con


def create_tables():
    """Create all tables at startup"""
    questions_table = '''CREATE TABLE IF NOT EXISTS questions(
                    questionId serial NOT NULL,
                    timestamp timestamp default current_timestamp,
                    createdBy SMALLINT NOT NULL,
                    meetup SMALLINT NOT NULL,
                    title varchar (100) NOT NULL,
                    body varchar (100) NOT NULL,
                    votes SMALLINT NOT NULL
                );
                '''
    meetups_table = '''CREATE TABLE IF NOT EXISTS meetups(
                    meetupId serial PRIMARY KEY NOT NULL,
                    createdOn TIMESTAMP DEFAULT NOW(),
                    location varchar NOT NULL,
                    meetup_images TEXT [],
                    topic varchar (250) NOT NULL,
                    description varchar (250) NOT NULL,
                    happeningOn varchar (50) NOT NULL,
                    meetup_tags TEXT []
                );
                '''
    users_table = '''CREATE TABLE IF NOT EXISTS users(
                    userId serial PRIMARY KEY NOT NULL,
                    firstname varchar (50) NOT NULL,
                    lastname varchar (50) NOT NULL,
                    othername varchar (50) NOT NULL,
                    email varchar (100) NOT NULL,
                    phoneNumber varchar (14) NOT NULL,
                    username varchar (50) NOT NULL,
                    registered boolean NOT NULL,
                    isAdmin boolean NOT NULL DEFAULT False,
                    password varchar (250) NOT NULL,
                    timestamp TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc')
                );
                '''

    comments_table = '''CREATE TABLE IF NOT EXISTS comments(
                    commentId serial PRIMARY KEY,
                    questionId INTEGER NOT NULL,
                    title varchar (100) NOT NULL,
                    body varchar (100) NOT NULL,
                    comment varchar (100) NOT NULL        
                );
                '''

    rsvp_table = '''CREATE TABLE IF NOT EXISTS rsvp(
                    rsvpId serial PRIMARY KEY,
                    meetupId INTEGER NOT NULL,
                    userId Integer  NOT NULL,
                    reply varchar (100) NOT NULL                            
                )
                '''


                   

    queries = [users_table, questions_table, comments_table, meetups_table, rsvp_table]
    con = con_return()
    for query in queries:
        cur = con.cursor()
        cur.execute(query)
    con.commit()

def add_admin():
    """Add admin to users Table""" 
    con = con_return()
    cur = con.cursor()
    encrypted_password = generate_password_hash("admin")
    cur.execute(query = "INSERT INTO users (firstname, lastname, othername, email, phoneNumber, username, registered, isAdmin, password) SELECT * FROM (SELECT 'admin', 'admin', 'admin', 'admin@gmail.com','0756998153', 'admin', True, True, '{}') AS tmp WHERE NOT EXISTS (SELECT username FROM users WHERE username = 'admin') LIMIT 1".format(encrypted_password)
    )
    con.commit()

    


def destroy_tables():
    """Method to delete tables"""
    con = con_return()
    cur = con.cursor()
    tables = ['meetups', 'questions', 'comments', 'rsvp']
    for table in tables:
        cur.execute("DELETE FROM {};".format(table))
    cur.execute("DELETE FROM users where username != 'admin';")
    con.commit()

