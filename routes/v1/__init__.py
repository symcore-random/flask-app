from flask import Blueprint

from .response_routes import responseroutes
from .tag_routes import tagroutes

v1_routes = Blueprint('v1_routes', __name__)
v1_routes.register_blueprint(responseroutes, url_prefix='/response')
v1_routes.register_blueprint(tagroutes, url_prefix='/tag')