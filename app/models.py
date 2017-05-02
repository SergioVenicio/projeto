# -*- coding: utf-8 -*-

import csv
import os
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager


class State(db.Model):
    __tablename__ = 'states'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(20), nullable=False)
    acronym = db.Column(db.String(2), nullable=False)
    cities = db.relationship('City', backref='state', lazy='dynamic')

    @staticmethod
    def populate():
        ''' All states of Federative Republic of Brazil '''
        basedir = os.path.abspath(os.path.dirname('__file__'))
        path = os.path.join(basedir, 'seeds', 'states.csv')
        with open(path) as f:
            reader = csv.DictReader(f)
            states = [State(description=row['ESTADO'], acronym=row['ACRONIMO'])
                      for row in reader]
        db.session.bulk_save_objects(states)
        db.session.commit()

    def __repr__(self):
        return '<State %r>' % self.description


class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50))
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'))
    providers = db.relationship('Provider', backref='city', lazy='dynamic')

    @staticmethod
    def populate():
        ''' All cities of federative republic of brazil '''
        states = {s.description: int(s.id) for s in State.query.all()}
        basedir = os.path.abspath(os.path.dirname('__file__'))
        path = os.path.join(basedir, 'seeds', 'cities.csv')
        with open(path) as f:
            reader = csv.DictReader(f)
            cities = [City(description=row['CIDADE'],
                      state_id=states[row['UF']]) for row in reader]
        db.session.bulk_save_objects(cities)
        db.session.commit()

    def __repr__(self):
        return '<City %r>' % self.description


class Provider(db.Model):
    __tablename__ = 'providers'
    id = db.Column(db.Integer(), primary_key=True)
    social_reason = db.Column(db.String(255), nullable=False)
    cnpj = db.Column(db.String(15), nullable=False)
    state_registration = db.Column(db.String(25), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    district = db.Column(db.String(60), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    email = db.Column(db.String(255))
    telephone = db.Column(db.String(15))
    products = db.relationship('Product', backref='provider', lazy='dynamic')

    def __repr__(self):
        return '<Provider %r>' % self.social_reason


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255))
    description = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float(asdecimal=True), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(2))
    manufactured = db.Column(db.DateTime)
    validity = db.Column(db.DateTime)
    provider_id = db.Column(db.Integer, db.ForeignKey('providers.id'))

    def __repr__(self):
        return '<Product %r>' % self.description


class UserType(db.Model):
    __tablename__ = 'user_types'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    users = db.relationship('User', backref='user_type', lazy='dynamic')

    @staticmethod
    def populate():
        roles = [
            (u'Administrador', 'admin'),
            (u'Usuário', 'user')
        ]
        for d, r in roles:
            role = UserType(description=d, role=r)
            db.session.add(role)
            db.session.commit()

    def __repr__(self):
        return '<UserTypes %r>' % self.description


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_types.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def has_permission(self, *roles):
        return self.user_type.role in roles

    def __repr__(self):
        return '<User %r>' % self.name


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
