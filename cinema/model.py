from . import db
import flask_login

class User(flask_login.UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    booked = db.relationship('MovieReservation', backref='user', lazy=True)
    # role = 1 manager 0 user
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(240), unique=False, nullable=False)
    director = db.Column(db.String(60), unique=False, nullable=False)
    description = db.Column(db.String(512), unique=False, nullable=True)
    img = db.Column(db.String(512))

    projected = db.relationship('Projection', backref='movie', lazy=True)

class Screen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    num_of_sits = db.Column(db.Integer, unique=False, nullable=False)

    projected = db.relationship('Projection', backref='screen', lazy=True)

class Projection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime(), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    screen_id = db.Column(db.Integer, db.ForeignKey('screen.id'))

    movie_booked = db.relationship('MovieReservation', backref='projectiond', lazy=True)

class MovieReservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    projection_id = db.Column(db.Integer, db.ForeignKey('projection.id'), nullable=False)
    num_of_seats = db.Column(db.Integer)

