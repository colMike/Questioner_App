"""RSVP models"""
from app.api.v1.utils.manage import fetch_one_meetup
from app.api.v1.utils.manage import find_username

reservation = []

class RsvpModel():
    """The meetup Rsvp Model Class"""
    def __init__(self):
        """Initializing the Meetup Model Class"""
        self.db = reservation 
        
    def make_reservation(self, reply):
        """Adding New Meetups"""    
        rsvp_data = {
            "id": 1,
            "meetup": 1,
            "user": 5,
            "reply": reply
        }

        self.db.append(rsvp_data)
        return self.db