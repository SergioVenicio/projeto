# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import (IntegerField, SelectField, StringField,
                     SubmitField, validators)


class ProductForm(FlaskForm):
    id = IntegerField()
    provider_id = SelectField(u'Fornecedor', choices=(), validators=[
        validators.Required()])
    description = StringField('Descrição', [
        validators.Required(),
        validators.Length(max=100)])
    unit = StringField('Unidade de Medida', [
        validators.Required(),
        validators.Length(max=2)])
    submit = SubmitField(u'Salvar alterações')
