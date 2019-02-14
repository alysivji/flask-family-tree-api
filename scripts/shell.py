from family_tree.app import create_app, db  # noqa
from family_tree.models import Person  # noqa

app = create_app()
app.app_context().push()
