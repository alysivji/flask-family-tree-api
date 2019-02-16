from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from .models import *  # noqa

migrate = Migrate()

cors = CORS()
