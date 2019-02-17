from flask import blueprints

from .person import PersonAPI, PersonItemAPI
from .relationship import RelationshipAPI
from .sandbox import SandboxAPI

familytree_bp = blueprints.Blueprint("family_tree", __name__)

familytree_bp.add_url_rule("/person", view_func=PersonAPI.as_view("person_api"))
familytree_bp.add_url_rule(
    "/person/<id>", view_func=PersonItemAPI.as_view("person_item_api")
)
familytree_bp.add_url_rule(
    "/person/<id>/relationship",
    view_func=RelationshipAPI.as_view("relationship_item_api"),
)

familytree_bp.add_url_rule("/sandbox", view_func=SandboxAPI.as_view("sandbox_api"))
