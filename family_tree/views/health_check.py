from flask import blueprints
from flask import jsonify

blueprint = blueprints.Blueprint('health_check', __name__)


@blueprint.route('/health_check', methods=['GET'])
def health_check():
    return jsonify(True)
