import datetime
import dateutil.tz

from flask import Blueprint, render_template

from . import model

from flask_login import current_user 
# current_user variable will also be available with the 
# data of the currently authenticated user. 

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    movies = model.Movie.query.all()
    users = model.User.query.all()
    return render_template("main/index.html", posts=movies, users=users)

@bp.route("/user")
def user():
    # try:
    result = model.MovieProjection.query.all()
    return render_template("user.html", data=result)
    # except Exception as e:
    #     # e holds description of the error
    #     error_text = "<p>The error:<br>" + str(e) + "</p>"
    #     hed = '<h1>Something is broken.</h1>'
    #     return hed + error_text
