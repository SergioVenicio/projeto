# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import (IntegerField, SelectField, StringField,
                     SubmitField,FloatField, validators)


class ProductForm(FlaskForm):
    id = IntegerField()
    provider_id = SelectField(u'Fornecedor', choices=(), validators=[
        validators.Required()])
    description = StringField('Descrição', [
        validators.Required(),
        validators.Length(max=100)])
    value =  FloatField('Valor', validators=[
        validators.Required()
    ])
    qntd = StringField(u'Quantidade', validators=[
        validators.Required()
    ])
    unit = StringField('Unidade de Medida', [
        validators.Required(),
        validators.Length(max=2)])
    submit = SubmitField(u'Salvar alterações')
