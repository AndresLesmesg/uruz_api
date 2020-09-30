from app import db


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
