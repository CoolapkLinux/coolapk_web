from flask import (
        Blueprint
        )

bp = Blueprint("topic_page", __name__)

@bp.route("/t/<string:topic_n>")
def topic_page(topic_n):
    return topic_n
