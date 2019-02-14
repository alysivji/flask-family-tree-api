"""Collection of utility functions for Family Tree application"""
import json
from flask import Response


def make_response(
    status_code: int = 200, *, headers: dict = {}, data: dict = {}, error: dict = {}
):
    """Build and send response"""
    resp = {"data": None, "error": None}
    if data:
        resp["data"] = data
    if error:
        resp["error"] = error

    return Response(
        status=status_code,
        headers=headers,
        content_type="application/json",
        response=json.dumps(resp),
    )
