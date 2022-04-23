import json
from flask import jsonify, make_response, request, g

from datetime import datetime

from models.tag_model import Tag


def get_all():
    pipeline = []
    tags_raw = Tag.objects().aggregate(pipeline)
    tags = json.loads(json.dumps(list(tags_raw), default=str))
    return make_response(jsonify(tags), 200)


def get_by_id(id):
    pipeline = []
    tags_raw = Tag.objects(id=id).aggregate(pipeline)
    tags = json.loads(json.dumps(list(tags_raw), default=str))
    tag = tags[0] if tags else {}
    return make_response(jsonify(tag), 200)


def create():
    tag_saved_raw = Tag(**request.json).save()
    tag_saved_id = json.loads(tag_saved_raw.to_json())['_id']['$oid']
    pipeline = []  # for population of objects
    tag_raw = Tag.objects(id=tag_saved_id).aggregate(pipeline)
    tag = json.loads(json.dumps(list(tag_raw), default=str))[0]
    return make_response(jsonify(tag), 200)


def update(id):
    Tag.objects(id=id).update(**request.json, updated_at=datetime.utcnow)
    pipeline = []  # for population of objects
    tag_raw = Tag.objects(id=id).aggregate(pipeline)
    tag = json.loads(json.dumps(list(tag_raw), default=str))[0]
    return make_response(jsonify(tag), 200)


def remove(id):
    # Tag.objects(id=id).delete()
    # In very rare occasions, the database removes documents entirely
    # What one usually does is to update the document with {deleted:True}
    Tag.objects(id=id).update(updated_at=datetime.utcnow,
                              deleted_at=datetime.utcnow,
                              deleted=True)

    return make_response({'message': 'document successfully deleted'}, 200)
