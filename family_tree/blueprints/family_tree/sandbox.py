from flask.views import MethodView
from family_tree.utilities import make_response


class SandboxAPI(MethodView):

    def get(self):
        return make_response(200, data={"sandbox": "up and running"})
