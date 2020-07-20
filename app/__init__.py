from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from app.config import DevConfig
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

# from flask_socketio import SocketIO, emit

db = SQLAlchemy()
bcrypt = Bcrypt()
login = LoginManager()
migrate = Migrate()

# socketio = SocketIO()






def create_app(config=DevConfig):
    """Returns an initialized Flask application."""
    app = Flask(__name__)
    app.config.from_object(config)
    
    
    db.init_app(app)
    from app.auth import models
    from app.admin import models
    from app.staff import models    
    login.init_app(app)    
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    # socketio.init_app(app)    

    from app.auth import auth
    app.register_blueprint(auth)

    from app.admin import admin
    app.register_blueprint(admin)
    
    from app.staff import staff
    app.register_blueprint(staff)

    # @socketio.on('my event')
    # def test_message(message):
    #     emit('my response', {'data': 'got it!'})
    
    
    return app


    
    