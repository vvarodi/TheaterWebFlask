# Only view for manager user
from flask import request, redirect, url_for, render_template, Blueprint, flash
from flask_login import current_user
import flask_login
from . import model
from datetime import date, timedelta
from . import db 
from functools import wraps
from datetime import datetime
from flask.json import jsonify

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
    projections, num_results = manager_reservations_auxiliar()
    return render_template("manager_schedule.html", packed=zip(projections, num_results), projections=projections)


@bp.route("/delete/<int:id>")
@flask_login.login_required
@manager_only
def delete(id):
    current_data = model.Projection.query.get(id)
    db.session.delete(current_data)
    db.session.commit()
    flash("You have deleted a projection", 'success')
    return redirect(url_for("manager.schedule"))


@bp.route("/edit/<int:id>")
@flask_login.login_required
@manager_only
def edit(id):
    movies = model.Movie.query.all()
    screens = model.Screen.query.all()
    current_data = model.Projection.query.get(id)
    return render_template("manager_edit.html", movies=movies, screens=screens, current_data=current_data)


@bp.route("/edit/<int:id>", methods=["POST"])
@flask_login.login_required
@manager_only
def edit_post(id):
    movie = request.form.get("movie")
    screen = request.form.get("screen")
    day = request.form.get("day")
    time = request.form.get("time")
   
    day = datetime.strptime(day, "%Y-%m-%d").date()
    time = datetime.strptime(time, "%H:%M:%S").time()

    projection = model.Projection.query.filter(model.Projection.id == id).first()
    projection.day = day
    projection.time = time
    projection.movie_id = movie
    projection.screen_id = screen 

    db.session.commit()
    flash("You have edited a projection", 'success')
    return redirect(url_for("manager.schedule"))



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
    return redirect(url_for("manager.schedule"))


@bp.route("/reservations")
@flask_login.login_required
@manager_only
def reservations():
    projections, num_results = manager_reservations_auxiliar()
    return render_template("manager_reservations.html", packed=zip(projections, num_results), projections=projections)


@bp.route("/manager_reservation/<int:id>")
@flask_login.login_required
@manager_only
def manager_reservation(id):
    reservations = model.Reservation.query.filter(model.Reservation.projection_id == id).order_by(model.Reservation.date_time).all()
    return render_template("manager_reservation.html", reservations=reservations)


def manager_reservations_auxiliar():
    current_day = date.today()
    # Show one week future projections (by timedelta(days=3), timedelta(weeks=1))
    future = current_day + timedelta(weeks=1)  # or (days=7)
    past = current_day - timedelta(weeks=1)
    # MANAGER WILL SEE ONE WEEK BEFORE AND ONE WEEK LATTER FROM TODAY
    projections = model.Projection.query.filter(model.Projection.day <= future, model.Projection.day >= past).order_by(model.Projection.day.asc(), model.Projection.time.asc()).all()
    num_results = []
    for proj in projections:
        num_results.append(proj.screen.num_total_seats - compute_reserved_seats(proj.id))
    return projections, num_results


def compute_reserved_seats(id):
    projection = model.Projection.query.filter(model.Projection.id == id).one()
    sum_result = db.session.query(
        db.func.sum(model.Reservation.num_seats).label('reserved')
    ).filter(
        model.Reservation.projection == projection
    ).one()
    num_reserved_seats = sum_result.reserved
    if (sum_result.reserved != None):
        num_free_seats = projection.screen.num_total_seats - num_reserved_seats
    else:
        num_free_seats = projection.screen.num_total_seats 
    # q = db.session.query(model.Reservation.projection_id, func.sum(model.Reservation.num_seats)).group_by(model.Reservation.projection_id).all()
    # for lst in q:
    #     num_reserved_seats = lst[1]
    #     if lst[0] == id:
    #         num_free_seats = projection.screen.num_total_seats - num_reserved_seats
    #         return  num_free_seats          
    return  num_free_seats






# AJAX
@bp.route('/ajax', methods=['POST', 'GET'])
def process_ajax():
    if request.method == "POST":
        projections = model.Projection.query.all()

        results = {}
        for proj in projections:
            seats = compute_reserved_seats(proj.id)
            # results[proj.id] = {'left':seats,'available': proj.screen.num_total_seats - seats}
            results[proj.id] = seats
        result = results
    return jsonify(result=result)


