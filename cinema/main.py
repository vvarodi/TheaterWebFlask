from datetime import date
import dateutil.tz

from flask import Blueprint, render_template, request
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
    nmovies = model.Projection.query.filter(model.Projection.day > current_day).all()  # limit(10) or without limit (maybe show all)
    tmovies = model.Projection.query.filter(model.Projection.day == current_day).all()

    movies = model.Movie.query.all()
    users = model.User.query.all()  # for debugging 
    return render_template("main/index.html", all_movies=movies, users=users, next_projections=nmovies, today_projections=tmovies)


# MOVIE VIEW OPEN FOR UNAUTHENTICATED USERS
@bp.route("/movie/<int:id>")
def movie(id):
    current_day = date.today().strftime('%Y-%m-%d')
    movie = model.Movie.query.get(id)
    projections = model.Projection.query.filter(model.Projection.movie_id == id).all()
    return render_template("movie.html", movie=movie, projections=projections)


@bp.route("/user")
@flask_login.login_required
def user():
    return render_template('user.html')


@bp.route("/reservation/", defaults={'id': None})
@bp.route("/reservation/<int:id>")
@flask_login.login_required
def reservation(id):
    all_projections = model.Projection.query.all()
    if id == None:
        return render_template("reservation.html", projection=None, projections=all_projections, all_projections=all_projections)
    else:
        projection = model.Projection.query.get(id)
        projections = model.Projection.query.filter(model.Projection.movie_id == projection.movie_id).all()
        return render_template("reservation.html", projection=projection, projections=projections, all_projections=all_projections)


@bp.route("/reservation/<int:id>", methods=["POST"])
@flask_login.login_required
def reservation_post(id):


    return render_template("reservation.html")








# @bp.route('/view')
# def show_view():
#     datos = model.Projection.query.all()
#     return render_template("view.html", datos=datos)

# @bp.route('/ajax', methods=["GET", "POST"])             
# def ajax():
#     if request.method == "POST":
#         search = request.form.get("projection")

#         projection = model.Projection.query.get(int(search))
#         return render_template("view.html", projection=projection)