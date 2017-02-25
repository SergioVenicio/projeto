# -*- coding: utf-8 -*-

from .. import db


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
