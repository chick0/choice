from flask import Blueprint
from flask import render_template

from app.fetch import one
from app.fetch import length

bp = Blueprint("choice", __name__, url_prefix="/")


@bp.get("")
def html():
    return render_template(
        "choice.html",
        menu=one(),
        length=length(),
    )
