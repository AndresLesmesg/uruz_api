from flask_restful import Resource, reqparse
from app.routine.models import Exercise

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


class Tag(Resource):
    pass


def request_null():
    return 'request null'


def request_successful():
    return 'successful transaction'


def output_format(data):
    data = clear_query(data)
    print(data)
    item = data.split(',')
    result = {}
    for i in item:
        value = i.split(':')
        print(value)
        result[value[0]] = value[1]

    return result


def output_format_all(data):
    data = clear_query(data)
    item_list = data.split(', ')
    result = {}
    dict_list = []

    for x in item_list:

        x = clear_query(x)
        item = x.split(',')
        print(item)

        for i in item:

            value = i.split(':')
            print(value)
            result[value[0]] = value[1]
        dict_list.append(result)

    return dict_list


def clear_query(data):
    data = str(data)
    if data[0] == '[' or data[0] == '(':
        data = data.replace(data[0], '')
        data = data.replace(data[len(data)-1], '')

    return data
