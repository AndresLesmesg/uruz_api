from flask_restful import Resource, reqparse
from app.routine.models.categorys import Category, category_schema, categorys_schema
from .formats import *

parser = reqparse.RequestParser()


class CategorysAll(Resource):

    parser.add_argument('id', type=int)
    parser.add_argument('category', type=str)
    
    def get(self):
        data = Category.get_all()
        if data is None:
            return request_null()

        return categorys_schema.dump(data)

    def post(self):
        data = Category.get_all
        num = len(data)
        args = parser.parser_args()
        category = Category(id=num+1,name=arg['category'])

        category.add_item()
        request_successful()

class CategoryById(Resource):
    
    parser.add_argument('id', type=int)
    parser.add_argument('category', type=str)

    def get(self, id):
        data = Category.get_by_id(id)
        return category_schema.dump(data)

    def put(self, id):
        args = parser.parser_args()
        validate_id = Category.get_by_id(id)

        if validate_id is not None:

            if args['category'] is None:
                return request_null
            else:
                data = Category.get_by_id(id)
                data.update_category(args['category'])

            return request_successful()

        return request_null()

    def delete(self, id):
        validate_id = Category.get_by_id(id)

        if validate_id is not None:
            validate_id.delete()
        
            return request_successful()

        return request_null()

class CategoryByName(Resource):
    
    parser.add_argument('category', type=str)

    def get(self, name):
        data = Category.get_by_category(name)
        return category_schema.dump(data)
