from flask import Blueprint

from .response_routes import responseroutes

v1_routes = Blueprint('v1_routes', __name__)
v1_routes.register_blueprint(responseroutes, url_prefix='/response')