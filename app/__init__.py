from flask import Flask
from instance.config import APP_CONFIG
from instance.db_con import create_tables

from .api.v2.views.user_views import user_version2
from .api.v2.views.meetup_views import meetup_version2
from .api.v2.views.question_views import question_version2


     
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('config.py')

    create_tables()
    
    app.register_blueprint(user_version2, url_prefix='/api/v2/')
    app.register_blueprint(meetup_version2, url_prefix='/api/v2/')
    app.register_blueprint(question_version2, url_prefix='/api/v2/')


    return app  
