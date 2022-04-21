from flask import Flask

from routes import all_routes

app = Flask(__name__)
app.register_blueprint(all_routes)
