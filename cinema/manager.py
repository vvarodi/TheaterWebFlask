# Only view for manager user
from functools import wraps
from flask import request, redirect, url_for, render_template, Blueprint
from flask_login import current_user
import flask_login
from . import model

bp = Blueprint("manager", __name__)

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
