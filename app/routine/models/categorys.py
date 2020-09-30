from app import db


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
