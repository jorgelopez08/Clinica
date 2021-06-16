from flask import Flask

from .models import db
from .config import Config
from .views import views
from .auth import auth


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app


