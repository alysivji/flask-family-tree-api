"""I would this add to manage.py, but this script is a good enough workaround"""

from family_tree.app import create_app,db


def init_db():
    app = create_app()
    app.app_context().push()
    db.create_all()


if __name__ == "__main__":
    init_db()
