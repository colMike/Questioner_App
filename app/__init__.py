from flask import Flask, Blueprint
from .api.v1.views.user_views import user_version1

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_version1, url_prefix='/api/v1/')
        
    return app
