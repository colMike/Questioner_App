"""Importing flask psycopg2"""
import os
import psycopg2



"""Create a Database Connection"""
config = os.getenv("APP_SETTINGS")


def con_return():
    if config == "development":
        db_url = os.getenv("DEV_DATABASE_URL")
        con = psycopg2.connect(db_url)
        return con

    else:
        db_url = os.getenv("TEST_DATABASE_URL")
        con = psycopg2.connect("dbname='questioner' host='localhost' port='5432' user='postgres' password='postgres'")
        return con
    


def create_tables():
    
    questions_table= '''CREATE TABLE IF NOT EXISTS questions(
                    questionId serial PRIMARY KEY,
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
                    userId INTEGER NOT NULL,
                    createdOn TIMESTAMP DEFAULT NOW(),
                    location varchar NOT NULL,
                    images varchar [],
                    topic varchar NOT NULL,
                    happeningOn TIMESTAMP NOT NULL,
                    tags varchar []
                );
                '''
    users_table = '''CREATE TABLE IF NOT EXISTS users(
                    userId serial PRIMARY KEY,
                    firstname varchar (50) NOT NULL,
                    lastname varchar (50) NOT NULL,
                    othername varchar (50) NOT NULL,
                    email varchar (100) NOT NULL,
                    phoneNumber varchar (14) NOT NULL,
                    username varchar (50) NOT NULL,
                    registered boolean NOT NULL,
                    isAdmin boolean NOT NULL,
                    password varchar (100) NOT NULL,
                    timestamp timestamp default current_timestamp
                );
                '''

    comments_table = '''CREATE TABLE IF NOT EXISTS comments(
                    commentId serial PRIMARY KEY,
                    questionId INTEGER NOT NULL,
                    title varchar (100) NOT NULL,
                    body varchar (100) NOT NULL,
                    comment varchar (100) NOT NULL        
                );'''


    
    queries = [users_table, questions_table, comments_table, meetups_table]
    con = con_return()
    for query in queries:
        cur = con.cursor()
        cur.execute(query)
    con.commit()
    con.close()


def destroy_tables():
    """Method to delete tables"""
    con = con_return()
    cur=con.cursor()
    query = """DROP TABLE IF EXISTS users, meetups, questions, rsvps, comments CASCADE;"""
    cur.execute(query)
    con.commit()
    con.close()