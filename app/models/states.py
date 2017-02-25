#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import db

class State(db.Model):
    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(20), nullable=False)
    acronym = db.Column(db.String(2), nullable=False)
    cities = db.relationship('City', backref='state', lazy='dynamic')

    @staticmethod
    def insert_states():
        states = [
            State(description='ACRE', acronym='AC'),
            State(description='ALAGOAS', acronym='AL'),
            State(description='AMAPA', acronym='AP'),
            State(description='AMAZONAS', acronym='AM'),
            State(description='BAHIA', acronym='BA'),
            State(description='CEARA', acronym='CE'),
            State(description='DISTRITO FEDERAL', acronym='DF'),
            State(description='ESPIRITO SANTO', acronym='ES'),
            State(description='GOIAS', acronym='GO'),
            State(description='MARANHAO', acronym='MA'),
            State(description='MATO GROSSO DO SUL', acronym='MS'),
            State(description='MATO GROSSO', acronym='MT'),
            State(description='MINAS GERAIS', acronym='MG'),
            State(description='PARAIBA', acronym='PB'),
            State(description='PARANA', acronym='PR'),
            State(description='PARA', acronym='PA'),
            State(description='PERNAMBUCO', acronym='PE'),
            State(description='PIAUI', acronym='PI'),
            State(description='RIO DE JANEIRO', acronym='RJ'),
            State(description='RIO GRANDE DO NORTE', acronym='RN'),
            State(description='RIO GRANDE DO SUL', acronym='RS'),
            State(description='RONDONIA', acronym='RO'),
            State(description='RORAIMA', acronym='RR'),
            State(description='SANTA CATARINA', acronym='SC'),
            State(description='SAO PAULO', acronym='SP'),
            State(description='SERGIPE', acronym='SE'),
            State(description='TOCANTINS', acronym='TO')
        ]
        db.session.bulk_save_objects(states)
        db.session.commit()

    def __repr__(self):
        return '<State %r>' % self.description
