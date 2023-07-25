from flask import Blueprint, Response, jsonify

blueprint = Blueprint("gumballs", __name__)


@blueprint.route("/")
def index() -> Response:
    return jsonify({"body": "It works!"})
