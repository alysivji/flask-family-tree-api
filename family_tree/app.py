from flask import Flask

from .extensions import cors, db
from .views import health_check


def create_app(*, testing=False):
    app = Flask(__name__)

    # use environment variables if in prod
    if testing:
        app.config["TESTING"] = True
        database_uri = "sqlite:///:memory:"
    else:
        database_uri = "sqlite:///../db.sqlite"

    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    cors.init_app(app)

    app.register_blueprint(health_check.blueprint, url_prefix='/api')
    return app
