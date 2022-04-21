from flask import Blueprint, g

from controllers import response_controllers
from middlewares.authCheck import token_change

responseroutes = Blueprint('response', __name__)
responseroutes.before_request(token_change)

responseroutes.get("/")(response_controllers.get_all)
responseroutes.get("/<string:id>")(response_controllers.get_by_id)
responseroutes.post("/")(response_controllers.create)
responseroutes.put("/<string:id>")(response_controllers.update)
responseroutes.delete("/<string:id>")(response_controllers.remove)
