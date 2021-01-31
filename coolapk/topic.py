from flask import (
        Blueprint
        )

bp = Blueprint("topic", __name__, url_prefix="/t/<string:topic_name>")
