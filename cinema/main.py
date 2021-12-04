import datetime
import dateutil.tz

from flask import Blueprint, render_template

from . import model

import flask_login 
# current_user variable will also be available with the 
# data of the currently authenticated user. 

bp = Blueprint("main", __name__)

@bp.route("/")
# @flask_login.login_required
# MAIN VIEW OPEN FOR UNAUTHENTICATED USERS
def index():
    movies = model.Movie.query.all()
    users = model.User.query.all()
    return render_template("main/index.html", posts=movies, users=users)


