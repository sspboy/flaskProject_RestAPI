from flask import Blueprint
from flask_restful import Api


login_blueprint = Blueprint('login', __name__)

api = Api(login_blueprint)

# login