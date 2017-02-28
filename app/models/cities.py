# -*- coding: utf-8 -*-

import csv
import os
from .. import db
from .states import State


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
