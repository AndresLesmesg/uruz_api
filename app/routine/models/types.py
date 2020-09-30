from app import db


class Type(db.Model):
    __tablename__ = 'types'
    # define
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, nullable=False)

    # constructor
    def __init__(self, id, name):
        self.id = id
        self.name = name

    # __repr__
    def __repr__(self):
        return "building"
    # methods
    pass
