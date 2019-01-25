"""Meetup models"""
import datetime

from instance.db_con import con_return

meetups = []


class MeetupModels():
    """The meetup Models Class"""

    def __init__(self):
        """Initializing the User Model Class"""
        self.con = con_return()
        self.cur = self.con.cursor()

    def add_meetup(self, location, meetup_images, topic, happeningOn, meetup_tags, description):
        """Adding New Meetups"""

        query = "SELECT * FROM meetups WHERE topic= '{}' AND happeningOn= '{}';".format(topic, happeningOn)
        self.cur.execute(query)

        data = self.cur.fetchone()

        if data:
            return False
        else:


            tags = "{"

            for tag in meetup_tags:
                tags += '"' + tag + '",'

            tags = tags[:-1] + '}'

            images = "{"

            for image in meetup_images:
                images += '"' + image + '",'

            images = images[:-1] + '}'

            query = "INSERT INTO meetups (location, meetup_images, topic, description, happeningOn, meetup_tags) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(
                location, images, topic, description, happeningOn, tags)

            self.cur.execute(query)
            self.con.commit()

            query = "SELECT * FROM meetups WHERE topic= '{}';".format(topic)
            self.cur.execute(query)

            data = self.cur.fetchone()

            meetup = {
                "meetupId": data[0],
                "Created On": data[1],
                "location": data[2],
                "Images": data[3],
                "topic": data[4],
                "description": data[5],
                "Happening On": data[6],
                "Tags": data[7]

            }

            return meetup

    def get_all_meetups(self):
        """Return all meetups"""
        self.cur.execute("SELECT * FROM meetups")
        data = self.cur.fetchall()

        all_meetups = []
        for item in data:

            payload = {
                "meetupId": item[0],
                "Created On": item[1],
                "Location": item[2],
                "Meetup Images": item[3],
                "Topic": item[4],
                "Happening On": item[5],
                "Meetup Tags": item[6],
            }
            all_meetups.append(payload)

        return all_meetups

    def get_one_meetup(self, meetupId):
        """Return specific meetups"""

        query = "SELECT * FROM meetups WHERE meetupId= '{}';".format(meetupId)
        self.cur.execute(query)

        data = self.cur.fetchone()

        if data:
             return data
        else:
             return None

    def rsvp_for_meetup(self, meetupId):
        """Make an RSVP for a meetup"""
        query = "SELECT * FROM meetups WHERE meetupId= '{}';".format(meetupId)
        self.cur.execute(query)

        data = self.cur.fetchone()

        if data:
             return data
        else:
             return None

    def delete(self, meetupId):
        """Delete a single Meetup"""
        query = "DELETE FROM meetups WHERE meetupId= '{}';".format(meetupId)
        self.cur.execute(query)
        self.con.commit()
        
