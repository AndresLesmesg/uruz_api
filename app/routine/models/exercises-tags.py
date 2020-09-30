from app import db
from .exercises import Exercise
from .tags import Tag


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
        return Tag.query.filter_by(tag_id=id)

    def add_item(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
