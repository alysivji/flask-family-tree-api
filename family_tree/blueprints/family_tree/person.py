from flask import request
from flask.views import MethodView

from family_tree.exceptions import NotFoundError
from family_tree.extensions import db
from family_tree.models import Person
from family_tree.schemas import person_list_schema, person_item_schema
from family_tree.utilities import make_response


class PersonAPI(MethodView):

    def get(self):
        all_people = Person.query.all()  # TODO pagination
        data = person_list_schema.dump(all_people)
        return make_response(200, data=data)

    def post(self):
        person = person_item_schema.load(request.json, session=db.session)
        db.session.add(person)
        db.session.commit()
        # TODO generate url dynamically (blueprint is throwing it in /api namespace)
        headers = {"Location": f"/api/v1/person/{person.id}"}
        data = person_item_schema.dump(person)
        return make_response(201, headers=headers, data=data)


class PersonItemAPI(MethodView):

    def get(self, id):
        person = Person.query.filter_by(id=id).first()
        if not person:
            raise NotFoundError("Person")

        data = person_item_schema.dump(person)
        return make_response(200, data=data)

    def put(self, id):
        person = Person.query.filter_by(id=id).first()
        if not person:
            raise NotFoundError("Person")

        person.patch(request.json)
        db.session.add(person)
        db.session.commit()
        data = person_item_schema.dump(person)
        return make_response(200, data=data)

    def delete(self, id):
        person = Person.query.filter_by(id=id).first()
        if not person:
            raise NotFoundError("Person")

        db.session.delete(person)
        db.session.commit()

        return make_response(200, data={})
