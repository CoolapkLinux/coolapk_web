from flask import (
        Blueprint, session, render_template
        )
from coolapk.coolapk_app.main_page import main_page

bp = Blueprint("coolapk", __name__, url_prefix="/")

@bp.route("/")
def main():
    if not "firstItem" in session.keys():
        session["firstItem"] = 0
    main_json = main_page(session["firstItem"])

    return render_template("index.html",data=main_json)
