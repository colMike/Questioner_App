"""Meetup models"""
from app.api.v1.utils.manage import fetch_one

meetups = [{
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
    
    def add_meetup(self, createdOn, location, images, topic, happeningOn, tags):
        """Adding New Meetups"""
        meetup_data = {
                "id": len(meetups) + 1,   
                "createdOn": createdOn,
                "location": location,
                "images": images,
                "topic": topic, 
                "happeningOn": happeningOn,
                "tags": tags
        }
        meetup_info = meetups.append(meetup_data)
        return meetup_info
    

    def get_all_meetups(self):
        """Return all questions"""
        return meetups

    def get_one_meetup(self, meetupId):
        """Return specific meetups"""
        return fetch_one(meetups, meetupId)