from flask import Blueprint
from flask import jsonify

from app.fetch import one

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.get("/menu")
def get_menu():
    return jsonify({
        "name": one()
    })
