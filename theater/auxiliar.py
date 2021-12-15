from flask import request, redirect, url_for, render_template, Blueprint
from flask_login import current_user
import flask_login
from . import model
from datetime import date, timedelta
from . import db 
from functools import wraps
from datetime import datetime
from flask.json import jsonify

bp = Blueprint("auxiliar", __name__)

def manager_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role != model.UserRole.manager:
            return redirect(url_for('auth.login', next=request.url))
        if current_user.role == model.UserRole.manager:
            return f(*args, **kwargs)
    return decorated_function

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