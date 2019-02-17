import itertools
from sqlalchemy.ext.hybrid import hybrid_property
from . import BaseModel
from ..extensions import db


def flatten(listOfLists):
    """Flatten one level of nesting

    From https://docs.python.org/3/library/itertools.html#itertools-recipes
    """
    return list(itertools.chain.from_iterable(listOfLists))


class Person(BaseModel):
    """Represents an individual person"""

    email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)

    birthdate = db.Column(db.DateTime, nullable=True)

    address = db.Column(db.String(255), nullable=True)
    phone_number = db.Column(db.String(255), nullable=True)

    # did not use backref as I like auto-complete
    parents = db.relationship(
        "Person",
        secondary="progeny",
        primaryjoin="Person.id==progeny.c.parent_id",
        secondaryjoin="Person.id==progeny.c.child_id",
        lazy="joined",
    )
    children = db.relationship(
        "Person",
        secondary="progeny",
        primaryjoin="Person.id==progeny.c.child_id",
        secondaryjoin="Person.id==progeny.c.parent_id",
        lazy="joined",
    )

    spouse = db.relationship(
        "Person",
        secondary="spouse",
        primaryjoin="Person.id==spouse.c.person_id",
        secondaryjoin="Person.id==spouse.c.spouse_person_id",
        lazy="joined",
    )

    @hybrid_property
    def grandchildren(self):
        return flatten([child.children for child in self.children])

    @hybrid_property
    def cousins(self):
        two_generations_up = flatten([parent.parents for parent in self.parents])
        aunts_uncles = set(flatten([person.children for person in two_generations_up])) - set(self.parents)
        return flatten([person.children for person in aunts_uncles])
