import os

from flask import Flask
from coolapk.coolapk import bp
from coolapk.topic import bp as bp_topic


def create_app() -> Flask:
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    # 主页
    app.register_blueprint(bp)
    app.add_url_rule("/", endpoint="index")
    # 话题
    app.register_blueprint(bp_topic)

    return app
