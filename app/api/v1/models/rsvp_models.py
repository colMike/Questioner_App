"""RSVP models"""
from app.api.v1.utils.manage import fetch_one_meetup



reservations = [{
            "id": 1,
            "meetup": 1,
            "user": 5,
            "reply": "yes"
        }]

class RsvpModels:
    """The meetup Rsvp Model Class"""
    def __init__(self):
        """Initializing the Meetup Model Class"""
        pass
        
    def make_reservation(self, reply):
        """Adding Reservation"""    
        rsvp_data = {
            "id": 1,
            "meetup": 1,
            "user": 5,
            "reply": reply
        }

        reservations.append(rsvp_data)
        return reservations