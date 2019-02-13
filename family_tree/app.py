from flask import Flask

from .extensions import cors, db
from .views import health_check


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    cors.init_app(app)

    app.register_blueprint(health_check.blueprint, url_prefix='/api')
    return app
