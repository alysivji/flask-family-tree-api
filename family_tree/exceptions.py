"""Application Level Exceptions

Implemented pattern described in Flask documentation
    http://flask.pocoo.org/docs/1.0/patterns/apierrors/
"""


class FamilyTreeException(Exception):
    """Custom application level Exception"""

    pass


class NotFoundError(FamilyTreeException):
    status_code = 404

    def __init__(self, object_type):
        super().__init__()
        self.message = f"{object_type} not found"
