"""RSVP models"""
from instance.db_con import con_return

reservations = []


class RsvpModels:
    """The meetup Rsvp Model Class"""

    def __init__(self):
        """Initializing the User Model Class"""
        self.con = con_return()
        self.cur = self.con.cursor()

    def make_reservation(self, reply, meetup_id):
        """Adding Reservation"""

        userId = 6

        query = "SELECT * FROM rsvp WHERE userId= '{}';".format(userId)
        self.cur.execute(query)

        data = self.cur.fetchone()

        if data:
            return None
        else:
            query = "INSERT INTO rsvp (meetupId, userId, reply) VALUES ('{}', '{}', '{}')".format(
                meetup_id, userId, reply)

            self.cur.execute(query)

            self.con.commit()
            query = "SELECT * FROM rsvp WHERE meetupId= '{}';".format(meetup_id)
            self.cur.execute(query)

            data = self.cur.fetchone()

            payload = {

                "meetupId": data[1],
                "UserId": data[2],
                "Reply": data[3]
            }

            return payload
