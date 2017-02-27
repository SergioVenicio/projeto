# -*- coding: utf-8 -*-

from flask import Flask
from flask_script import Shell, Server
from flask_migrate import MigrateCommand
from .extensions import db, login_manager, manager, migrate
from .models import (User, UserType, State, City, Provider, Product)
from .controllers import controller


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config)
    configure_extensions(app)
    configure_blueprints(app)
    configure_comands(app)
    return app


def configure_blueprints(app):
    app.register_blueprint(controller)


def configure_extensions(app):
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    login_manager.login_message = u'Autentique-se para acessar esta página'
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app)
    manager.app = app
    migrate.db = db


def configure_comands(app):
    manager.add_command('runserver', Server(threaded=True))
    manager.add_command('shell', Shell(make_context=MakeShellContext(
        app, User, UserType, Provider, Product, State, City)))
    manager.add_command('db', MigrateCommand)

    @manager.command
    def createdb():
        confirm = input(
            'Do you really want to continue? (Y/N)?'
            ' All data will be deleted! ')
        if confirm.upper() == 'Y':
            with app.app_context():
                db.drop_all()
                db.create_all()
                UserType.insert_roles()
                State.insert_states()
                City.insert_cities()


class MakeShellContext():
    '''
    Creates a callable wrap to flask-script shell

    :param app: application object
    :param models: list of model objects
    '''

    def __init__(self, app, *models):
        self._app = app
        self._models = dict((m.__name__, m) for m in models)

    def __call__(self):
        return dict(app=self._app, db=db, **self._models)
