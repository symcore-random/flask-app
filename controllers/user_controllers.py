import json
from flask import jsonify, make_response, request, g
from werkzeug.security import generate_password_hash

from models.user_model import User


def register():
    try:
        username = request.json['username']
        password_hash = generate_password_hash(request.json['password'])
        credentials = {'username': username, 'password': password_hash}
        
        user_saved = User(**credentials).save()
        user_saved_id = json.loads(user_saved.to_json())['_id']['$oid']
        pipeline = []  # for population of objects
        user_raw = User.objects(id=user_saved_id).aggregate(pipeline)
        user = json.loads(json.dumps(list(user_raw), default=str))[0]
        return make_response(jsonify(user), 200)
    except Exception as err:
        return make_response(jsonify({"message": str(err)}), 400)
