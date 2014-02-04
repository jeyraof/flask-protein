"""
Write down application instance initializing.
"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__, static_path='/static')
    register_blueprints(app)

    return app


def register_blueprints(machine):
    from importlib import import_module
    import os
    for app in [f for f in os.listdir('app/modules') if not os.path.isfile(f)]:
        try:
            views = import_module('app.modules.%s.views' % app)
            machine.register_blueprint(views.bp)
        except ImportError as e:
            print e
            pass

db = SQLAlchemy()