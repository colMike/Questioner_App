# Questioner_App
Crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize questions to be answered. Other users can vote on asked questions and they bubble to the top.

## Badges
[![Build Status](https://travis-ci.org/colMike/Questioner_App.svg?branch=develop)](https://travis-ci.org/colMike/Questioner_App)
[![BCH compliance](https://bettercodehub.com/edge/badge/colMike/Questioner_App?branch=develop)](https://bettercodehub.com/)
[![Coverage Status](https://coveralls.io/repos/github/colMike/Questioner_App/badge.svg?branch=develop)](https://coveralls.io/github/colMike/Questioner_App?branch=develop)


## Background Knowledge
This branch contains the API Endpoints for Questioner platform

## Endpoints
This platform has the following endpoints

#### Meetup Endpoints

Method | Endpoint | Purpose
--- | --- | ---
POST | /meetups | Create a meetup record
POST | /meetups/int:meetup-id/rsvps | Respond to meetup RSVP
GET | /meetups/int:meetup-id | Fetch a specific meetup record
GET | /meetups/upcoming | Fetch all upcoming meetup records

#### Question Endpoints

Method | Endpoint | Purpose
--- | --- | ---
POST | /questions | Create a question for a specific meetup
PATCH | /questions/int:question-id/upvote | Upvote a specific question
PATCH | /questions/int:question-id/downvote | Downvote a specific question

#### User Endpoints

Method | Endpoint | Purpose
--- | --- | ---
POST | /auth/signup | Register a new users
POST | /auth/login | Log in  registered users
GET | /users | Fetch all registered users


## Prerequisites

- [VS Code](https://code.visualstudio.com)
- [Python 3.6](https://www.python.org)
- [Postgres](https://www.postgresql.org)
- [Insomnia](https://insomnia.rest) / [Postman](https://www.getpostman.com)

## Installation

- Clone this repository inside your working repository
```
```console
mike@mike:~$ git clone https://github.com/colMike/Questioner_App.git
```

- Create the psql databases

```console
mike@mike:~$ createdb questioner
mike@mike:~$ createdb test_questioner
```
```
Navigate into the cloned repository
```
mike@mike:~$ cd Questioner/
```
Switch to develop branch
```
mike@mike:~$ git checkout develop
```


### Installation
Set up a virtual environment

```
mike@mike:~$ virtualenv -p python3 venv
```

Activate the environment

```
mike@mike:~$ source venv/bin/activate
```
Install dependencies
```
mike@mike:~$ pip install -r requirements.txt
```

Run the application
```
mike@mike:~$ flask run
```

### Testing
Run the command
```
mike@mike:~$ pytest

```

### Heroku Deployment

This app is deployed on [Heroku] https://colmike-questioner-app.herokuapp.com/


#### Author 
Michael Mbugua - [MikeMbugua](https://colmike.github.io)
