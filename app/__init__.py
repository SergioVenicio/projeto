# -*- coding: utf-8 -*-

from flask import Flask
from flask_script import Shell, Server
from flask_migrate import MigrateCommand
from .extensions import db, login_manager, manager, migrate
from .models import (User, UserType, State, City, Provider, Product)
from .controllers import controller
from .utils.helpers import MakeShellContext, HandleError


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config)
    configure_extensions(app)
    configure_blueprints(app)
    configure_errors(app)
    configure_comands(app)
    return app


def configure_blueprints(app):
    app.register_blueprint(controller)


def configure_extensions(app):
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'controller.login'
    login_manager.login_message = u'Autentique-se para acessar esta página'
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app)
    manager.app = app
    migrate.db = db


def configure_comands(app):
    manager.add_command('runserver', Server(threaded=True))
    manager.add_command('shell', Shell(make_context=MakeShellContext(
        app, db, User, UserType, Provider, Product, State, City)))
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
                UserType.populate()
                State.populate()
                City.populate()


def configure_errors(app):
    errors = {
        404: 'Página não encontrada!',
        500: 'Erro interno do servidor!'
    }
    for code, message in errors.items():
        app.errorhandler(code)(HandleError('error.html', message))
