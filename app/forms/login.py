#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField)
from wtforms.validators import Required, Email


class LoginForm(FlaskForm):
    email = StringField('Digite seu e-mail', validators=[Required(), Email()])
    password = PasswordField('Digite sua senha', validators=[Required()])
    remember_me = BooleanField('Mantenha-me conectado')
    submit = SubmitField('Login')
