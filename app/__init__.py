"""
Write down application instance initializing.
"""

from flask import Flask
from importlib import import_module
from app.database import db
import os


def create_app(setting):
    app = Flask(__name__, static_path='/static')
    load_configs(app, setting)
    register_blueprints(app)
    db.init_app(app)
    db.app = app

    return app


def load_configs(machine, env):
    setting = import_module('settings.%s' % env)
    machine.config.update(setting.config)


def register_blueprints(machine):
    modules = (lambda x: [f for f in os.listdir(x) if os.path.isdir(os.path.join(x, f))])('app/modules')
    load_views(machine, modules)
    load_models(modules)


def load_views(machine, modules):
    if len(modules) > 0:
        print 'Loading views:::'
        for module in modules:
            try:
                views = import_module('app.modules.%s.views' % module)
                machine.register_blueprint(views.bp)
                print '=> Successfully loaded: %s.views' % module

            except ImportError as e:
                print '=> Failed loading: %s.views | %s', (module, e)
                pass

        print '=> Complete.\n'
    else:
        print 'There is no module to load. Pass the process.'


def load_models(modules):
    if len(modules) > 0:
        print 'Loading models:::'
        for module in modules:
            try:
                import_module('app.modules.%s.models' % module)
                print '=> Successfully loaded: %s.models' % module

            except ImportError as e:
                print '=> Failed loading: %s.models | %s', (module, e)
                pass

        print '=> Complete.\n'
    else:
        print 'There is no module to load. Pass the process.'