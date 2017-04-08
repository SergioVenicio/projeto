# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import (IntegerField, SelectField, StringField,
                     SubmitField, validators)
from wtforms.fields.html5 import EmailField
from ..models.cities import City


class ProviderForm(FlaskForm):
    id = IntegerField()
    social_reason = StringField('Razão Social', [
        validators.Required(), validators.Length(min=3, max=255)])
    cnpj = StringField('CNPJ', [
        validators.Required(), validators.Length(min=17, max=18)])
    state_registration = StringField('Inscrição Estadual', [
        validators.Required(), validators.Length(min=10, max=25)])
    address = StringField('Endereço', [
        validators.required(), validators.Length(min=3, max=255)])
    district = StringField('Bairro', [
        validators.required(), validators.Length(min=3, max=60)])
    city_id = SelectField(u'Cidade', choices=(), validators=[
        validators.Required()])
    email = EmailField(u'Email')
    telephone = StringField(u'Telefone', [
        validators.Required(), validators.Length(min=14, max=15)])
    submit_provider = SubmitField(u'Salvar alterações')

    def fill_city(self, id):
        city = City.query.get(id)
        if city:
            self.city_id.choices = [(city.id, city.description)]
            self.city_id.data = city.id
            self.city_id.errors = []
        else:
            return False
