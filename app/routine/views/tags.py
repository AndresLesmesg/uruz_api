from flask_restful import Resource, reqparse
from app.routine.models.tags import Tag, tag_schema, tags_schema
from .formats import *

parser = reqparse.RequestParser()


class TagsAll(Resource):

    parser.add_argument('id', type=int)
    parser.add_argument('tag', type=str)
    
    def get(self):
        data = Tag.get_all()
        if data is None:
            return request_null()

        return tags_schema.dump(data)

    def post(self):
        data = Tag.get_all
        num = len(data)
        args = parser.parser_args()
        tag = Tag(id=num+1,name=arg['tag'])

        tag.add_item()
        request_successful()

class TagById(Resource):
    
    parser.add_argument('id', type=int)
    parser.add_argument('tag', type=str)


    def get(self, id):
        data = Tag.get_by_id(id)
        return tag_schema.dump(data)

    def put(self, id):
        args = parser.parser_args()
        validate_id = Tag.get_by_id(id)

        if validate_id is not None:

            if args['tag'] is None:
                return request_null
            else:
                data = Tag.get_by_id(id)
                data.update_tag(args['tag'])

            return request_successful()

        return request_null()

    def delete(self, id):
        validate_id = Tag.get_by_id(id)

        if validate_id is not None:
            validate_id.delete()
        
            return request_successful()

        return request_null()

class TagByName(Resource):
    
    parser.add_argument('tag', type=str)

    def get(self, name):
        data = Tag.get_by_tag(name)
        return tag_schema.dump(data)
