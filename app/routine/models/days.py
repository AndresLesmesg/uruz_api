from app import db

class Day(db.Model):
    __tablename__ = 'days'
    # define
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(80), nullable=False)
    routine_id = db.Column(db.Integer, db.ForeignKey('routines.id'))

    # constructor
    def __inint__(self, id, day, routine_id):
        self.id = id
        self.day = day
        self.routine_id = routine_id

    # __repr__
    def __repr__(self):
        return "building"
    # methods
    pass
