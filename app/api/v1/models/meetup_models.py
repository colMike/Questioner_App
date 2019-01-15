"""Meetup models"""
import datetime

from app.api.v1.utils.manage import fetch_one_meetup

meetups = [{
    "meetupId": 1,
    "createdOn": "25th Dec 2018",
    "location": "Taj Mall, Nairobi",
    "images": ["Food.jpg", "Kitchen.jpg"],
    "topic": "Making Pasta", 
    "happeningOn":  "2nd Jan 2019, 09:40AM",
    "tags":  ["Art", "Homestudy"]
}]



class MeetupModels:
    """The meetup Models Class"""
    def __init__(self):
        """Initializing the Meetup Model Class"""
        pass
    
    def add_meetup(self, location, images, topic, happeningOn, tags):
        """Adding New Meetups"""
        meetup_data = {
                "meetupId": len(meetups) + 1,   
                "createdOn": datetime.datetime.now(),
                "location": location,
                "images": images,
                "topic": topic, 
                "happeningOn": happeningOn,
                "tags": tags
        }
        meetups.append(meetup_data)
        return meetups
    

    def get_all_meetups(self):
        """Return all meetups"""
        return meetups

    def get_one_meetup(self, meetupId):
        """Return specific meetups"""
        return fetch_one_meetup(meetups, meetupId)

    def rsvp_for_meetup(self, meetupId):
        """Make an RSVP for a meetup"""
        return fetch_one_meetup(meetups, meetupId)



        