from flask import blueprints
from .sandbox import SandboxAPI

familytree_bp = blueprints.Blueprint("family_tree", __name__)

familytree_bp.add_url_rule("/sandbox", view_func=SandboxAPI.as_view("sandbox_api"))
