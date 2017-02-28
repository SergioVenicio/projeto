#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField)
from wtforms.validators import Required, Email


class LoginForm(Form):
    email = StringField('Digite seu e-mail', validators=[Required(), Email()])
    password = PasswordField('Digite sua senha', validators=[Required()])
    remember_me = BooleanField('Mantenha-me conectado')
    submit = SubmitField('Login')
