from flask import Flask, Blueprint
from .api.v1.views.user_views import user_version1


APP = Flask(__name__)

APP.register_blueprint(user_version1, url_prefix='/api/v1/')
       
