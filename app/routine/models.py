from app import db


class Exercise(db.Model):
    __tablename__ = 'exercises'
    # define
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    src = db.Column(db.String(256), nullable=True)

    # constructor
    def __init__(self, id, name, src):
        self.id = id
        self.name = name
        self.src = src

    # __repr__
    def __repr__(self):
        return "(id:{},name:{},src:{})".format(self.id,
                                               self.name,
                                               self.src)

    # methods
    @staticmethod
    def get_all():
        return Exercise.query.all()

    @staticmethod
    def get_by_id(id):
        return Exercise.query.filter_by(id=id).first()

    @staticmethod
    def get_by_name(name):
        return Exercise.query.filter_by(name=name).first()

    def add_item(self):
        db.session.add(self)
        db.session.commit()

    def update_name(self, name):
        self.name = name
        db.session.commit()

    def update_src(self, src):
        self.src = src
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Tag(db.Model):
    __tablename__ = 'tags'

    # define
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(25), nullable=False)

    # constructor
    def __init__(self, id, tag):
        self.id = id
        self.tag = tag

    # __repr__
    def __repr__(self):
        return "(id:{},name:{})".format(self.id, self.tag)

    # methods
    @staticmethod
    def get_all():
        return Tag.query.all()

    @staticmethod
    def get_by_id(id):
        return Tag.query.get(id).firrst()

    @staticmethod
    def get_by_tag(tag):
        return Tag.query.get(tag).first()

    def add_item(self):
        db.session.add(self)
        db.session.commit()

    def update_tag(self, tag):
        self.tag = tag
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class ExerciseTag(db.Model):
    __tablename__ = 'exercises_tags'
    # define
    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
    # relationship plane

    # constructor
    def __init__(self, id, tag, exercises):
        self.id = id
        self.tag_id = tag
        self.exercise_id = exercises

    # __repr__
    def __repr__(self):
        return "(id:{},exercise:{},tag:{})".format(self.id,
                                                   self.exercise_id,
                                                   self.tag_id)

    # methods
    @staticmethod
    def get_by_id(id):
        return Exercise.query.get(id).first()

    @staticmethod
    def get_exercise_by_id(id):
        return Exercise.query.filter_by(exercise_id=id)

    @staticmethod
    def get_tag_by_id(id):
        return Exercise.query.filter_by(tag_id=id)

    def add_item(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


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


class Routine(db.Model):
    __tablename__ = 'routines'
    # define
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    # constructor
    def __init__(self, id, name):
        self.id = id
        self.name = name

    # __repr__
    def __repr__(self):
        return "buoliding"
    # methods
    pass


class Category(db.Model):
    __tablename__ = 'categorys'
    # define
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)

    # constructor
    def __init__(self, id, category):
        self.id = id
        self.category = category

    # __repr__
    def __repr__(self):
        return "building"
    # methods
    pass


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


class TrainerType(db.Model):
    __tablename__ = 'trainers_types'
    # define
    id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))

    # constructor
    def __init__(self, id, trainer_id, type_id):
        self.id = id
        self.type_id = type_id
        self.trainer_id = trainer_id

    # __repr__
    def __repr__(self):
        return "building"
    # methods
    pass


def create():
    db.create_all()
    db.commit()


def delete():
    db.drop_all()
    db.commit()
