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
        # for a given person
        pass


# class PersonItemAPI(MethodView):

#     def get(self, id):
#         person = Person.query.filter_by(id=id).first()
#         if not person:
#             raise NotFoundError("Person")

#         data = person_item_schema.dump(person).data
#         return make_response(200, data=data)

#     def put(self, id):
#         person = Person.query.filter_by(id=id).first()
#         if not person:
#             raise NotFoundError("Person")

#         person.patch(request.json)
#         db.session.add(person)
#         db.session.commit()
#         data = person_item_schema.dump(person).data
#         return make_response(200, data=data)

#     def delete(self, id):
#         person = Person.query.filter_by(id=id).first()
#         if not person:
#             raise NotFoundError("Person")

#         db.session.delete(person)
#         db.session.commit()

#         return make_response(200, data={})
