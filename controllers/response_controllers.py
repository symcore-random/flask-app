import json
from flask import jsonify, make_response, request, g
from helpers.utils import lookup

from models.response_model import Response


def get_all():
    pipeline = [lookup('tag:_id', 'tag_ids')]  # for population of objects
    responses_raw = Response.objects().aggregate(pipeline)
    responses = json.loads(json.dumps(list(responses_raw), default=str))
    return make_response(jsonify(responses), 200)


def get_by_id(id):
    pipeline = [lookup('tag:_id', 'tag_ids')]  # for population of objects
    responses_raw = Response.objects(id=id).aggregate(pipeline)
    response = json.loads(json.dumps(list(responses_raw), default=str))[0]
    return make_response(jsonify(response), 200)


def create():
    return make_response(
        {'message': f'g_token:{g.token} method:{request.method}'}, 200)


def update(id):
    return make_response(
        {'message': f'g_token:{g.token} method:{request.method} id:{id}'}, 200)


def remove(id):
    return make_response(
        {'message': f'g_token:{g.token} method:{request.method} id:{id}'}, 200)


# Create a text-based post
# tag1 = Tag(tag='tag1')
# tag2 = Tag(tag='tag2')
# tag1.save()
# tag2.save()
# tag1_dic = json.loads(tag1.to_json())
# print(tag1_dic['_id'])
# response = Response(
#     title='Using MongoEngine',
#     content='See the tutorial',
#     tags=['62621f69c23202', '62621f69c2d6aa93e2ca1302'])
# response.save()

# obj = Response.objects(id='62621da018fac71747b78dc5').aggregate(
#     {
#         "$lookup": {
#             "from": "tag",  # Tag collection database name
#             "foreignField": "_id",  # Primary key of the Tag collection
#             "localField": "tags",  # Reference field
#             "as": "tags",
#         }
#     })
# pprint(list(obj))

# print(json.loads(obj.to_json()))
