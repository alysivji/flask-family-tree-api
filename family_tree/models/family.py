from . import BaseModel
from ..extensions import db


class Family(BaseModel):
    """Represents a family"""

    name = db.Column(db.String(255), unique=True, nullable=False)

    crest = db.Column(db.String(255), nullable=True)
    origin = db.Column(db.String(255), nullable=True)

    head_of_family_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    head_of_family = db.relationship("Person", uselist=False)

    # many to many with people
    members = None
