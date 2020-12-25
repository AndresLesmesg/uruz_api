from flask_restful import Resource, reqparse
from app.routine.models.types import Type, type_schema, types_schema
from .formats import *

parser = reqparse.RequestParser()


class TypesAll(Resource):

    parser.add_argument('id', type=int)
    parser.add_argument('type', type=str)
    
    def get(self):
        data = Type.get_all()
        data = output_format_all(data)
        if data is None:
            return request_null()

        return types_schema.dump(data)

    def post(self):
        data = Type.get_all
        num = len(data)
        args = parser.parser_args()
        type_ = Type(id=num+1,name=arg['type'])

        type_.add_item()
        request_successful()

class TypeById(Resource):
    
    parser.add_argument('id', type=int)
    parser.add_argument('type', type=str)


    def get(self, id):
        data = Type.get_by_id(id)
        return type_schema.dump(data)

    def put(self, id):
        args = parser.parser_args()
        validate_id = Type.get_by_id(id)

        if validate_id is not None:

            if args['type'] is None:
                return request_null
            else:
                data = Type.get_by_id(id)
                data.update_type(args['type'])

            return request_successful()

        return request_null()

    def delete(self, id):
        validate_id = Type.get_by_id(id)

        if validate_id is not None:
            validate_id.delete()
        
            return request_successful()

        return request_null()

class TypeByName(Resource):
    
    parser.add_argument('type', type=str)

    def get(self, name):
        data = Type.get_by_type(name)
        return type_schema.dump(data)
