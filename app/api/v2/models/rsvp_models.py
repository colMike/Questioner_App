"""RSVP models"""
from app.api.v2.utils.manage import fetch_one_meetup



reservations = []

class RsvpModels:
    """The meetup Rsvp Model Class"""
    def __init__(self):
        """Initializing the Meetup Model Class"""
        pass
        
    def make_reservation(self, reply):
        """Adding Reservation"""    
        rsvp_data = {
            "id": len(reservations) + 1,
            "meetup": len(reservations) + 1,
            "user": 5,
            "reply": reply
        }

        reservations.append(rsvp_data)
        return reservations