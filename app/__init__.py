#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Istancia das extensoes
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message = u'Autentique-se para acessar esta página'


def create_app(config=None):
    app = Flask('app')
    app.config.from_object(config)

    # Blueprints
    #from controllers import view
    #app.register_blueprint(view)

    # Configuração das extensões
    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
