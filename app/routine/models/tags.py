from app import db


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
