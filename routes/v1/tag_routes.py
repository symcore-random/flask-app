from flask import Blueprint, g

from controllers import tag_controllers
from middlewares.authCheck import token_change

tagroutes = Blueprint('tag', __name__)
tagroutes.before_request(token_change)

tagroutes.get("/")(tag_controllers.get_all)
tagroutes.get("/<string:id>")(tag_controllers.get_by_id)
tagroutes.post("/")(tag_controllers.create)
tagroutes.put("/<string:id>")(tag_controllers.update)
tagroutes.delete("/<string:id>")(tag_controllers.remove)
