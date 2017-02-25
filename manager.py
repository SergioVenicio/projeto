#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.models import (User, UserType, State, City, Provider, Product)

app = create_app(config='config.Development')
manager = Manager(app)
migrate = Migrate(app, db)

@manager.command
def createdb():
    confirm = input(
        "Você deseja realmente continuar (S/N)? Todos"
        " os dados serão apagados! "
    )
    if confirm.upper() == 'S':
        with app.app_context():
            db.drop_all()
            db.create_all()
            UserType.insert_roles()
            State.insert_states()
            City.insert_cities()

def make_shell_context():
    return dict(
        app=app, db=db, User=User, UserType=UserType,
        Provider=Provider, Product=Product, State=State, City=City
    )

manager.add_command('runserver', Server(threaded=True))
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
