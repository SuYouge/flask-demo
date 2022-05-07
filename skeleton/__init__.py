from flask import Flask
from skeleton.blueprints.task1 import task1_bp
from skeleton.blueprints.home import home_bp
from skeleton.extensions import csrf, bootstrap, scheduler
import os

def create_app():
    app = Flask("skeleton")
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "some secret")
    register_blueprints(app)
    register_extensions(app)
    return app

def register_blueprints(app):
    app.register_blueprint(task1_bp)
    app.register_blueprint(home_bp)

def register_extensions(app):
    csrf.init_app(app)
    bootstrap.init_app(app)
    scheduler.init_app(app)