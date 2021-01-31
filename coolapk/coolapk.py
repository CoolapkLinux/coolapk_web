from flask import (
        Blueprint, session, render_template, redirect, url_for
        )
from coolapk.coolapk_app.main_page import main_page

bp = Blueprint("coolapk", __name__, url_prefix="/")

@bp.route("/")
def main():
    if not "firstItem" in session.keys():
        session["firstItem"] = 0

    main_json = main_page(session["firstItem"])
    print(main_json)

    if not session["firstItem"] == 0:
        if session["firstItem"] == main_json[-1]["id"]:
            return render_template("index.html", data=main_json, nomore=True)

    session["firstItem"] = main_json[-1]["id"]

    return render_template("index.html",data=main_json)

@bp.route("/clearSession")
def clear():
    session.pop("firstItem",None)
    return redirect(url_for("index"))
