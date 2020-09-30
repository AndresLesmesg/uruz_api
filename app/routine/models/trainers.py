from app import db


class Trainer(db.Model):
    __tablename__ = 'trainers'
    # define
    id = db.Column(db.Integer, primary_key=True)
    plane_id = db.Column(db.Integer,  db.ForeignKey('planes.id'))
    day_id = db.Column(db.Integer,  db.ForeignKey('days.id'))

    # constructor
    def __init__(self, id, plane_id, day_id):
        self.id = id
        self.day_id = day_id
        self.plane_id = plane_id

    # __repr__
    def __repr__(self):
        return "building"
    # methods
    pass
