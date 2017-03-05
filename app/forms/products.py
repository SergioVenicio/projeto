# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import (DateField, IntegerField, SelectField, StringField,
                     SubmitField, FloatField, validators)


class ProductForm(FlaskForm):
    id = IntegerField()
    provider_id = SelectField(u'Fornecedor', choices=(), validators=[
        validators.Required()])
    description = StringField('Descrição', [
        validators.Required(),
        validators.Length(max=100)])
    value = FloatField('Valor', validators=[
        validators.Required()
    ])
    quantity = StringField(u'Quantidade', validators=[
        validators.Required()
    ])
    unit = StringField('Unidade de Medida', [
        validators.Required(),
        validators.Length(max=2)])
    manufactured = DateField(u'Fabricação', format='%d/%m/%Y')
    validity = DateField(u'Validade', format='%d/%m/%Y')
    submit_product = SubmitField(u'Salvar alterações')
