from marshmallow_sqlalchemy import ModelSchema

from ..models import Person


class PersonSchema(ModelSchema):
    class Meta:
        model = Person
