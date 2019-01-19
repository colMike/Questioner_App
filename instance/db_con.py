"""Importing flask psycopg2"""
import os
import psycopg2

"""connect using psycopg """

url = "dbname='questioner' host='localhost' port='5432' user='colmike' password='colmic76'" 

# creating the connection
con = psycopg2.connect(url)

db_url = os.getenv('DATABASE_URL')


# creating the cursor
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS questions(
        id serial PRIMARY KEY,
        title varchar (50) NOT NULL,
        description varchar (100) NOT NULL,
        timestamp timestamp default current_timestamp
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



# closing the connection
# con.close()
# 

# def connection(url):
#     con = psycopg2.connect(db_url)
#     return con

# def create_tables():
    # query1 = '''CREATE TABLE IF NOT EXISTS questions(
    #     id serial PRIMARY KEY,
    #     title varchar (50) NOT NULL,
    #     description varchar (100) NOT NULL,
    #     timestamp timestamp default current timestamp
    # )'''
    # query2 = '''CREATE TABLE IF NOT EXISTS users(
    #     id serial PRIMARY KEY,
    #     username varchar (50) NOT NULL,
    #     email varchar (100) NOT NULL,
    #     password varchar (100) NOT NULL,
    #     timestamp timestamp default current timestamp
    # )'''

#     queries =[query1, query2]

#     for q in queries:
#         cur.execute(q)



def destroy_tables():
    pass

