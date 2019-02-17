"""
Could improve use an improve abstraction versus if/else on relationship_type
"""

from flask import request
from flask.views import MethodView

from family_tree.exceptions import NotFoundError
from family_tree.extensions import db
from family_tree.models import Person
from family_tree.schemas import relationship_item_schema
from family_tree.utilities import make_response, deserialize_request


class RelationshipAPI(MethodView):

    def get(self):
        return make_response(405)

    def post(self, id):
        person = Person.query.filter_by(id=id).first()
        if not person:
            raise NotFoundError("Person")
        result = deserialize_request(relationship_item_schema, request.json)

        relation_type = result["relation_type"]
        if relation_type == "child":
            parent = person
            child = request._deserialized["person_id_for_relation_type"]
        elif relation_type == "parent":
            child = person
            parent = request._deserialized["person_id_for_relation_type"]

        parent.children.append(child)
        db.session.add(parent)
        db.session.add(child)
        db.session.commit()

        return make_response(201)

    def delete(self, id):
        person = Person.query.filter_by(id=id).first()
        if not person:
            raise NotFoundError("Person")
        result = deserialize_request(relationship_item_schema, request.json)

        relation_type = result["relation_type"]
        if relation_type == "child":
            parent = person
            child = request._deserialized["person_id_for_relation_type"]
        elif relation_type == "parent":
            child = person
            parent = request._deserialized["person_id_for_relation_type"]

        try:
            parent.children.remove(child)
        except ValueError:
            return make_response(404, error="person_id_for_relation_type is not a valid relation")

        db.session.add(parent)
        db.session.add(child)
        db.session.commit()
        return make_response(200)
