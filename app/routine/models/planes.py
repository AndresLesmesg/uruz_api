from app import db


class Plane(db.Model):
    __tablename__ = 'planes'
    # define
    id = db.Column(db.Integer, primary_key=True)
    unit = db.Column(db.String(10), nullable=True)
    number_set = db.Column(db.Integer, nullable=True)
    repetition = db.Column(db.Integer, nullable=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

    # constructor
    def __init__(self, id,  number_set, repetition, unit, exercise_id):
        self.id = id
        self.unit = unit
        self.repetition = repetition
        self.number_set = number_set
        self.exercise_id = exercise_id

    # __repr__
    def __repr__(self):
        id = self.id
        unit = self.unit
        reps = self.repetition
        number = self.number_set
        exercise = self.exercise_id

        return "(id:{},set:{},rep:{},unit:{},exercise:{})".format(id,
                                                                  number,
                                                                  reps,
                                                                  unit,
                                                                  exercise)

    # methods
    @staticmethod
    def get_all():
        return Plane.query.all()

    @staticmethod
    def get_by_id(id):
        return Plane.query.get(id).first()

    @staticmethod
    def get_exercise_by_id(id):
        return Plane.query.filter_by(exercise_id=id)

    def add_item(self):
        db.session.add(self)
        db.session.commit()

    def update_unit(self, unit):
        self.unit = unit
        db.session.commit()

    def update_repetition(self, repetition):
        self.repetition = repetition
        db.session.commit()

    def update_number_set(self, number_set):
        self.number_set = number_set
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


