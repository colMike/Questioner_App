"""RSVP models"""
from app.api.v1.utils.manage import fetch_one_meetup



reservations = []

class RsvpModels:
    """The meetup Rsvp Model Class"""
    def __init__(self):
        """Initializing the Meetup Model Class"""
        pass
        
    def make_reservation(self, reply,meetup_id):
        """Adding Reservation"""    
        rsvp_data = {
            "id": len(reservations) + 1,
            "meetup": meetup_id,
            "user": 5,
            "reply": reply
        }

        reservations.append(rsvp_data)
        return reservations