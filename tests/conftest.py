"""pytest plugins for Project

I was creating fixtures to ensure I'm working with the right application context and ran
into an issue while trying to configure an in-memory test database. Googling led me to a
blog post that implemented the fixtures I was going to create.

It was using callbacks for fixture teardown which is a deprecated pytest pattern. I
changed it to use generators. Why reinvent the wheel when you can just improve it?

The `client` fixture is the only fixture that I wrote from scratch.

References:
    - http://alexmic.net/flask-sqlalchemy-pytest/
    - http://flask.pocoo.org/docs/1.0/testing/
"""

import pytest

from family_tree.app import create_app
from family_tree.extensions import db as _db


@pytest.fixture(scope="session")
def app():
    """Session-wide test `Flask` application.

    Establish an application context before running the tests.
    """
    app = create_app(testing=True)
    ctx = app.app_context()
    ctx.push()
    yield app

    ctx.pop()


@pytest.fixture(scope="session")
def client(app):
    """Create flask test client where we can trigger test requests to app"""
    client = app.test_client()
    yield client


@pytest.fixture(scope="session")
def db(app):
    """Session-wide test database."""
    _db.app = app
    _db.create_all()
    yield _db

    _db.drop_all()


@pytest.fixture(scope="function")
def session(db):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()
    options = dict(bind=connection, binds={})

    session = db.create_scoped_session(options=options)
    db.session = session
    yield session

    transaction.rollback()
    connection.close()
    session.remove()
