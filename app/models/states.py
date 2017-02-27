#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import os
from .. import db


class State(db.Model):
    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(20), nullable=False)
    acronym = db.Column(db.String(2), nullable=False)
    cities = db.relationship('City', backref='state', lazy='dynamic')

    @staticmethod
    def insert_states():
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
