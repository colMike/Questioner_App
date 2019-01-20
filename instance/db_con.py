"""Importing flask psycopg2"""
import os
import psycopg2

"""connect using psycopg """

url = "dbname='questioner' host='localhost' port='5432' user='colmike' password='colmic76'" 
db_url = os.getenv('DATABASE_URL')

# creating the connection
con = psycopg2.connect(url)


# creating the cursor
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS questions(
        questionId serial PRIMARY KEY,
        timestamp timestamp default current_timestamp,
        createdBy SMALLINT NOT NULL,
        meetup SMALLINT NOT NULL,
        title varchar (100) NOT NULL,
        body varchar (100) NOT NULL,
        votes SMALLINT NOT NULL
    )''')

cur.execute('''CREATE TABLE IF NOT EXISTS users(
        UserId serial PRIMARY KEY,
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
    )''')

con.commit()

def destroy_tables():
    pass

