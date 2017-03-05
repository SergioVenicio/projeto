# -*- coding: utf-8 -*-

from .. import db


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(2))
    manufactured = db.Column(db.DateTime)
    validity = db.Column(db.DateTime)
    provider_id = db.Column(db.Integer, db.ForeignKey('providers.id'))

    def __repr__(self):
        return '<Product %r>' % self.description
