# Only view for manager user
from flask import request, redirect, url_for, render_template, Blueprint
from flask_login import current_user
import flask_login
from . import model
from datetime import date
from . import db 
from functools import wraps
from datetime import datetime

bp = Blueprint("manager", __name__)

def manager_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role != model.UserRole.manager:
            return redirect(url_for('auth.login', next=request.url))
        if current_user.role == model.UserRole.manager:
            return f(*args, **kwargs)
    return decorated_function

@bp.route("/schedule")
@flask_login.login_required
@manager_only
def schedule():
    current_day = date.today().strftime('%Y-%m-%d')
    projections = model.Projection.query.filter(model.Projection.day >= current_day).all()
    return render_template("manager_schedule.html", projections=projections)

@bp.route("/edit/<int:id>")
@flask_login.login_required
@manager_only
def edit(id):
    projection = model.Projection.query.get(id)
    movies = model.Movie.query.all()
    return render_template("edit_projection.html", projection=projection, movies=movies)


@bp.route("/edit/<int:id>", methods=["POST"])
@flask_login.login_required
@manager_only
def edit_post(id):
    projection = model.Projection.query.get(id)
    movies = model.Movie.query.all()

    movie_id = request.form.get("movie")
    if movie_id == "none":
        movie_id = projection.movie.id
    projection.movie_id = movie_id
    db.session.commit()

    return redirect(url_for("manager.schedule"))



#### delete latter




@bp.route("/add")
@flask_login.login_required
@manager_only
def add():
    movies = model.Movie.query.all()
    screens = model.Screen.query.all()
    current_day = date.today().strftime('%Y-%m-%d')
    return render_template("manager_add.html", movies=movies, screens=screens, current_day=current_day)

@bp.route("/add", methods=["POST"])
@flask_login.login_required
@manager_only
def add_post():
    movie = request.form.get("movie")
    screen = request.form.get("screen")
    day = request.form.get("day")
    time = request.form.get("time")
    time = time + ':00'
    day = datetime.strptime(day, "%Y-%m-%d").date()
    time = datetime.strptime(time, "%H:%M:%S").time()
    new_projection = model.Projection(day=day, time=time, movie_id=movie, screen_id=screen)
    db.session.add(new_projection)
    db.session.commit()
    return render_template("manager_schedule.html")





@bp.route("/reservations")
@flask_login.login_required
@manager_only
def reservations():
    reservations = model.Reservation.query.all()
    return render_template("manager_reservations.html", reservations=reservations)
