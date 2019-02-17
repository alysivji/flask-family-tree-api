from flask import request
from marshmallow import fields, post_load, Schema, validates, ValidationError
from ..models import Person


VALID_RELATION_TYPES = ["parent", "child"]


class RelationshipSchema(Schema):
    id = fields.Int(dump_only=True)
    relation_type = fields.Str(required=True)
    person_id_for_relation_type = fields.Int(required=True)

    # Validators
    @validates("relation_type")
    def validate_relation_type(self, data):
        relation_type = str(data).lower()
        if relation_type not in VALID_RELATION_TYPES:
            raise ValidationError(f"{relation_type} is not supported")

    @validates("person_id_for_relation_type")
    def validate_person_id_for_relation_type(self, data):
        person = Person.query.filter_by(id=data).first()
        if not person:
            raise ValidationError(f"person_id_for_relation_type is not in database")
        request._deserialized = {"person_id_for_relation_type": person}

    @post_load
    def make_relation(self, data):
        return data
