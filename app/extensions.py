# -*- coding: utf-8 -*-

from flask_login import LoginManager
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
manager = Manager()
migrate = Migrate()
