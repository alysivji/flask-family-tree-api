from marshmallow_sqlalchemy import ModelSchema

from ..models import Person


class PersonSchema(ModelSchema):
    class Meta:
        model = Person


person_item_schema = PersonSchema(many=False)
person_list_schema = PersonSchema(many=True)
