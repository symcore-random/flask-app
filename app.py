from flask import Flask
from dotenv import load_dotenv

from helpers.errors import not_found, bad_request, server_error
from routes import all_routes
from databases.mongodb import Mongodb

load_dotenv()

connection = Mongodb().create_connection()

app = Flask(__name__)
app.register_blueprint(all_routes)

app.errorhandler(404)(not_found)
app.errorhandler(400)(bad_request)
app.errorhandler(500)(server_error)
