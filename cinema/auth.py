from flask import Blueprint, render_template, request, redirect, url_for, flash
import flask_login

from . import db, bcrypt

from . import model

bp = Blueprint("auth", __name__)

@bp.route("/signup")
def signup():
    return render_template("auth/signup.html")


@bp.route("/signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    role = request.form.get("role")
    # Check that passwords are equal
    if password != request.form.get("password_repeat"):
        flash("Sorry, passwords are different")
        return redirect(url_for("auth.signup"))
    # Check if the email is already at the database
    user = model.User.query.filter_by(email=email).first()
    
    # same email for both roles possible???
    if user:
        flash("Sorry, the email you provided is already registered")
        return redirect(url_for("auth.signup"))
 
    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = model.User(email=email, name=username, password=password_hash, role=role)
    db.session.add(new_user)
    db.session.commit()
    flash("You've successfully signed up!")
    return redirect(url_for("auth.login"))


@bp.route("/login")
def login():
    return render_template("auth/login.html")


@bp.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    # Check that passwords are equal
    if password != request.form.get("password_repeat"):
        flash("Sorry, passwords are different")
        return redirect(url_for("auth.login"))
    # Get the user with that email from the database:
    user = model.User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        # The user exists and the password is correct
        flask_login.login_user(user)
        flash("You've successfully loged!")
        return redirect(url_for("main.index"))
    else:
        # Wrong email and/or password
        if user == None:
            flash("User not registered. Go to Sign Up.")
            return redirect(url_for("auth.login"))
        if user.email == email and bcrypt.check_password_hash(user.password, password) == 0:
            flash("Wrong password")
        return redirect(url_for("auth.login"))

@bp.route("/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    flash ('You have been logged out')
    return redirect(url_for("auth.login"))
