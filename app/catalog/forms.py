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
    submit_login = SubmitField('Login')


class AccountForm(FlaskForm):
    name = StringField('Digite seu nome', validators=[Required()])
    email = StringField('Digite seu e-mail', validators=[Required(), Email()])
    password = PasswordField('Digite sua senha', validators=[Required()])
    submit_account = SubmitField('Cadastrar')
