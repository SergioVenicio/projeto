# -*- coding: utf-8 -*-

from .. import db


class UserType(db.Model):
    __tablename__ = 'user_types'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    users = db.relationship('User', backref='user_type', lazy='dynamic')

    @staticmethod
    def insert_roles():
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
