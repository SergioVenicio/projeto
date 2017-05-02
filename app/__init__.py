# -*- coding: utf-8 -*-

from flask import Flask
from flask_script import Shell, Server
from getpass import getpass
from .extensions import db, login_manager, manager, migrate, MigrateCommand
from .models import (User, UserType, State, City, Provider, Product)
from .admin import admin
from .shop import shop
from .utils.helpers import MakeShellContext, HandleError


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config)
    configure_extensions(app)
    configure_blueprints(app)
    configure_template_filters(app)
    configure_comands(app)
    configure_errors(app)
    return app


def configure_blueprints(app):
    app.register_blueprint(admin)
    app.register_blueprint(shop)


def configure_extensions(app):
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'shop.login'
    login_manager.login_message = u'Autentique-se para acessar esta página'
    db.init_app(app)
    login_manager.init_app(app)
    manager.app = app
    migrate.init_app(app, db, 'migrations')


def configure_template_filters(app):
    @app.context_processor
    def utility_processor():
        def format_price(value, currency='R$'):
            return '{0} {1:.2f}'.format(currency, value)
        return dict(format_price=format_price)


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

    @manager.command
    def adduser():
        name = input('name: ')
        email = input('email: ')
        user_type_id = int(input('user type: admin / user (1 / 2): '))
        password = getpass(prompt='password: ')
        password2 = getpass(prompt='confirm password: ')
        if password != password2:
            import sys
            sys.exit(u'Error: the password don\'t match!')
        user = User(name=name, email=email,
                    user_type_id=user_type_id, password=password)
        db.session.add(user)
        db.session.commit()
        print('User {0} has been registered!'.format(name))


def configure_errors(app):
    errors = {
        404: 'Página não encontrada!',
        500: 'Erro interno do servidor!'
    }
    for code, message in errors.items():
        app.errorhandler(code)(HandleError('error.html', message))
