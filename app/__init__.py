from flask import Flask
from .api.v1.views.user_views import user_version1
from .api.v1.views.meetup_views import meetup_version1
from .api.v1.views.question_views import question_version1

from .api.v2.views.user_views import user_version2
from .api.v2.views.meetup_views import meetup_version2
from .api.v2.views.question_views import question_version2


     
def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_version1, url_prefix='/api/v1/')
    app.register_blueprint(meetup_version1, url_prefix='/api/v1/')
    app.register_blueprint(question_version1, url_prefix='/api/v1/')

    app.register_blueprint(user_version2, url_prefix='/api/v2/')
    app.register_blueprint(meetup_version2, url_prefix='/api/v2/')
    app.register_blueprint(question_version2, url_prefix='/api/v2/')


    return app  

