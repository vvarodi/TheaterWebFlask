from flask import Flask # making available the code we need to build web apps with flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy() # db object will be used to access the database when needed
bcrypt = Bcrypt()

def create_app(test_config=None):
    app = Flask(__name__) # create an instance of the Flask class for our web app

    # set configuration variables
    app.config["SECRET_KEY"] = b"\x8c\xa5\x04\xb3\x8f\xa1<\xef\x9bY\xca/*\xff\x12\xfb"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db' #path to database and its name
    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://22_appweb_31:9JoOBTaL@mysql.lab.it.uc3m.es/22_appweb_31c"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warnings
    
    # register db to the current app
    db.init_app(app)


    # User Authentication
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    # login_manager.login_message = "Login or Change role."
    login_manager.init_app(app)
    from . import model
    @login_manager.user_loader
    def load_user(user_id):
        return model.User.query.get(int(user_id))

    # register blueprints
    
    from . import main
    from . import auth
    from . import manager
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(manager.bp)

     # Create Database Models
    with app.app_context():
        db.create_all()

    return app

