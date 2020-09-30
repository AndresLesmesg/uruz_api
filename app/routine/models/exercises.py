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
