"""Contains all relationship type models.

Note: I originally started with a relationship schema and was going to have a
relationship_type schema, but that would have taken more time. I decided to
write to design for Direct Relationships between parents and children and maybe
add spousal relationships, if given enough time.
"""

from . import BaseModel
from ..extensions import db


class Progeny(BaseModel):
    """Not the best name, but too far in too modify.

    Might change at end, if enough time.
    """
    parent_id = db.Column(db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"))
    child_id = db.Column(db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"))


class Spouse(BaseModel):
    """Contains symmetrical entries

    A -> B | B -> A
    """
    person_id = db.Column(db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"))
    spouse_person_id = db.Column(db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"))
