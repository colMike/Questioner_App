# Questioner_App
Crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize questions to be answered. Other users can vote on asked questions and they bubble to the top.

## Badges
[![Build Status](https://travis-ci.org/colMike/Questioner_App.svg?branch=develop)](https://travis-ci.org/colMike/Questioner_App)
[![Coverage Status](https://coveralls.io/repos/github/colMike/Questioner_App/badge.svg?branch=develop)](https://coveralls.io/github/colMike/Questioner_App?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/50cb2021e6e046611714/maintainability)](https://codeclimate.com/github/colMike/Questioner_App/maintainability)
[![BCH compliance](https://bettercodehub.com/edge/badge/colMike/Questioner_App?branch=develop)](https://bettercodehub.com/)


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


### Pre-requisites
```
1. Python 3.6 or higher
2. Git
3. Virtualenv
4. Pytest
...with these permissions:
```
## Getting Started

Clone this repository inside your working repository
```
git clone https://github.com/colMike/Questioner_App.git

```
Navigate into the cloned repository
```
cd Questioner/
```
Switch to develop branch
```
git checkout develop
```


### Installation
Set up a virtual environment

```
virtualenv -p python3 venv
```

Activate the environment

```
source venv/bin/activate
```
Install dependencies
```
pip install -r requirements.txt
```

Run the application
```
flask run
```

### Testing
Run the command
```
pytest app/tests/v1

```

### Heroku Deployment

This app is deployed on [Heroku] https://colmike-questioner-app.herokuapp.com/


#### Author 
Michael Mbugua
