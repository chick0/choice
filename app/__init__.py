from os.path import abspath
from os.path import dirname

from flask import Flask
from flask import redirect
from flask import url_for

from app.fetch import KEY
from app.fetch import read


def create_app():
    app = Flask(__name__)
    app.config[KEY] = read(
        app_dir=dirname(abspath(__file__))
    )

    from app import views
    for v in views.__all__:
        app.register_blueprint(getattr(getattr(views, v), "bp"))

    app.register_error_handler(
        code_or_exception=404,
        f=lambda err: redirect(url_for("choice.html"))
    )

    return app
