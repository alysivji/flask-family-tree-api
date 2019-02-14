from .base import BaseModel
from ..extensions import db


class Person(BaseModel):
    """Represents an individual person"""

    email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)

    birthdate = db.Column(db.DateTime, nullable=True)

    address = db.Column(db.String(255), nullable=True)
    phone_number = db.Column(db.String(255), nullable=True)

    # which family they belong to (could be multiple, right?)
    # what relationships they have with other persons
