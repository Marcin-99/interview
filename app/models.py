from app import db
from datetime import datetime


'''Database model for stations.'''
class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coor_lat = db.Column(db.Float, nullable=False)
    coor_lng = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    date_modified = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    kWh_price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Station(id = {self.id}, coor_lat = {self.coor_lat}, lng = {self.coor_lng}, " \
               f"date created = {self.date_created}, date_modified = {self.date_modified}, kWh_price = {self.kWh_price}"