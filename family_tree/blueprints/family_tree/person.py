from flask.views import MethodView

# from family_tree.extensions import db
from family_tree.models import Person
from family_tree.schemas import person_schema
from family_tree.utilities import make_response


class PersonAPI(MethodView):

    def get(self):
        all_people = Person.query.all()
        data = person_schema.dump(all_people, many=True).data

        return make_response(200, data=data)
