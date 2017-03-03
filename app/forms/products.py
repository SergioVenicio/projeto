# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import (DateField, IntegerField, SelectField, StringField,
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
    fabrication = DateField(u'Fabricação', format='%d/%m/%Y')
    validaty = DateField(u'Validade', format='%d/%m/%Y')
    submit = SubmitField(u'Salvar alterações')
