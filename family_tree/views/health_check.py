from flask import blueprints
from flask import jsonify

healthcheck_bp = blueprints.Blueprint('health_check', __name__)


@healthcheck_bp.route('/health_check', methods=['GET'])
def health_check():
    return jsonify(True)
