from . import BaseModel
from ..extensions import db


class Progeny(BaseModel):
    parent_id = db.Column(db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"))
    child_id = db.Column(db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"))


class Spouse(BaseModel):
    """Contains symmetrical entries

    A -> B | B -> A
    """
    person_id = db.Column(db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"))
    spouse_person_id = db.Column(db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"))
