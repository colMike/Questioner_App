"""Meetup models"""
from app.api.v1.utils.manage import fetch_one_meetup

meetups = []
reservation = []



class MeetupsModel():
    """The meetup Models Class"""
    def __init__(self):
        """Initializing the Meetup Model Class"""
        self.db = meetups 
    
    def add_meetup(self, createdOn, location, images, topic, happeningOn, tags):
        """Adding New Meetups"""
        meetup_data = {
                "meetupId": len(meetups) + 1,   
                "createdOn": createdOn,
                "location": location,
                "images": images,
                "topic": topic, 
                "happeningOn": happeningOn,
                "tags": tags
        }
        self.db.append(meetup_data)

        return self.db
    

    def get_all_meetups(self):
        """Return all meetups"""
        return meetups

    def get_one_meetup(self, meetupId):
        """Return specific meetups"""
        return fetch_one_meetup(meetups, meetupId)

