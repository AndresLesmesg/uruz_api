from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

from app.config import Config


db = SQLAlchemy()
api = Api()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    # endpoints list
    from app.routine.views.exercises import ExercisesAll, ExerciseById, ExerciseByName
    api.add_resource(ExercisesAll, '/exercises/')
    api.add_resource(ExerciseById, '/exercises/<int:id>')
    api.add_resource(ExerciseByName, '/exercises/<string:name>')
    api.init_app(app)
    # blueprints

    return app
