from flask_restful import Resource, reqparse
from app.routine.models.exercises import Exercise
from .formats import *

parser = reqparse.RequestParser()


class ExercisesAll(Resource):
    parser.add_argument('id', type=int)
    parser.add_argument('name', type=str)
    parser.add_argument('src', type=str)

    def get(self):
        data = Exercise.get_all()
        data = output_format_all(data)
        if data is None:
            return request_null()

        return {'exercices': '{}'.format(clear_query(data))}

    def post(self):
        data = Exercise.get_all()
        num = len(data)
        args = parser.parse_args()
        exercise = Exercise(id=num+1,
                            name=args['name'],
                            src=args['src'])
        validate_id = Exercise.get_by_id(args['id'])

        if validate_id is None:
            exercise.add_item()
            return request_successful()

        return request_null()


class ExerciseById(Resource):
    parser.add_argument('name', type=str)
    parser.add_argument('src', type=str)

    def get(self, id):
        data = Exercise.get_by_id(id)
        print(data)
        data = output_format(data)
        return {'exercice': '{}'.format(data)}

    def put(self, id):
        args = parser.parse_args()
        validate_id = Exercise.get_by_id(id)

        if validate_id is not None:

            if args['name'] is None and args['src'] is None:
                return request_null

            if args['name'] is not None:
                data = Exercise.get_by_id(id)
                data.update_name(args['name'])

            if args['src'] is not None:
                data = Exercise.get_by_id(id)
                data.update_src(args['src'])

            return request_successful()

        return request_null()

    def delete(self, id):
        validate_id = Exercise.get_by_id(id)

        if validate_id is not None:
            validate_id.delete()


class ExerciseByName(Resource):
    parser.add_argument('id', type=int)
    parser.add_argument('name', type=str)
    parser.add_argument('src', type=str)

    def get(self, name):
        data = Exercise.get_by_name(name)
        return {'exercice': '{}'.format(data)}

    def post(self, name):
        data = Exercise.get_all()
        num = len(data)
        args = parser.parse_args()
        exercise = Exercise(id=num+1,
                            name=name,
                            src=args['src'])
        validate_name = Exercise.get_by_name(name)

        if validate_name is None:
            exercise.add_item()
            return request_successful()
        return request_null()

    def put(self, name):
        args = parser.parse_args()
        validate_name = Exercise.get_by_name(name)

        if validate_name is not None:

            if args['name'] is None and args['src'] is None:
                return request_null

            if args['src'] is not None:
                data = Exercise.get_by_name(name)
                data.update_src(args['src'])

            if args['name'] is not None:
                data = Exercise.get_by_name(name)
                data.update_name(args['name'])

            return request_successful()

        return request_null()

    def delete(self, name):
        validate_id = Exercise.get_by_name(name)

        if validate_id is not None:
            validate_id.delete()

