from datetime import date
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
    pmovies = model.Projection.query.order_by(model.Projection.day.desc()).limit(10).all()
    all_movies = model.Movie.query.all()
    users = model.User.query.all()
    current_day = date.today().strftime('%Y-%m-%d')

    return render_template("main/index.html", all_movies=all_movies, users=users, current_day=current_day, pmovies=pmovies)

