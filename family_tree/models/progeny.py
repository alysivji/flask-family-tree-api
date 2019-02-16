from . import BaseModel
from ..extensions import db


class Progeny(BaseModel):
    parent_id = db.Column(db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"))
    child_id = db.Column(db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"))
