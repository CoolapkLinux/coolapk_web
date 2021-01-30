import os

from flask import Flask
from coolapk.coolapk import bp


def create_app() -> Flask:
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    app.register_blueprint(bp)

    return app
