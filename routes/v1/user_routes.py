from flask import Blueprint, g

from controllers import user_controllers
from middlewares.auth_check import auth_check

userroutes = Blueprint('user', __name__)
userroutes.before_request(auth_check)

userroutes.post("/register")(user_controllers.register)
