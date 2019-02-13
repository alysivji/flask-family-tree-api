from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from .models import *  # noqa

cors = CORS()
