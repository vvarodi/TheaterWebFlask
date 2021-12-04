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





# Only view for manager user
from functools import wraps
from flask import g, request, redirect, url_for
from flask_login import current_user

def manager_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role != model.UserRole.manager:
            return redirect(url_for('auth.login', next=request.url))
        if current_user.role == model.UserRole.manager:
            return f(*args, **kwargs)
    return decorated_function

@bp.route("/manager")
@flask_login.login_required
@manager_only
def manager():
    return render_template("manager.html")
