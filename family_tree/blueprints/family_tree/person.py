from flask import request
from flask.views import MethodView

from family_tree.extensions import db
from family_tree.models import Person
from family_tree.schemas import person_list_schema, person_item_schema
from family_tree.utilities import make_response


class PersonAPI(MethodView):

    def get(self):
        all_people = Person.query.all()
        data = person_list_schema.dump(all_people).data
        return make_response(200, data=data)

    def post(self):
        person = person_item_schema.load(request.json, session=db.session).data
        db.session.add(person)
        db.session.commit()
        return make_response(201, data=person_item_schema.dump(person).data)
