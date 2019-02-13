from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from .views import health_check

db = SQLAlchemy()
cors = CORS()

from .models import *  # noqa


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    cors.init_app(app)

    app.register_blueprint(health_check.blueprint, url_prefix='/api')
    return app
