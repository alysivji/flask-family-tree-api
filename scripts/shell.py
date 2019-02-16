from family_tree.app import create_app, db  # noqa
from family_tree.models import *  # noqa

app = create_app()
app.app_context().push()
