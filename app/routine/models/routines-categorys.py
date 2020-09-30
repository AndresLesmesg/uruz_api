from app import db


class RoutineCategory(db.Model):
    __tablename__ = 'routines_categorys'
    # define
    id = db.Column(db.Integer, primary_key=True)
    routine_id = db.Column(db.Integer, db.ForeignKey('routines.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categorys.id'))

    # constructor
    def __init__(self, id, routine, category):
        self.id = id
        self.routine_id = routine
        self.category_id = category

    # __repr__
    def __repr__(self):
        return "building"
    # methods
    pass
