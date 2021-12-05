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
    current_day = date.today().strftime('%Y-%m-%d')
    pmovies = model.Projection.query.filter(model.Projection.day >= current_day).limit(10).all()
    tmovies = model.Projection.query.filter(model.Projection.day == current_day).all()

    all_movies = model.Movie.query.all()
    users = model.User.query.all()
    
    return render_template("main/index.html", movies=all_movies, users=users, pmovies=pmovies, tmovies=tmovies)

