# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import (
    DateField, IntegerField, PasswordField, SelectField, StringField,
    SubmitField, FloatField, validators, HiddenField
)
from wtforms.widgets.html5 import NumberInput
from wtforms.fields.html5 import EmailField

from ..models import Provider, City, UserType


class ProductForm(FlaskForm):
    id = IntegerField()
    provider_id = SelectField(u'Fornecedor', choices=(), validators=[
        validators.Required()])
    image = HiddenField('Imagem', validators=[validators.optional()])
    image_file = FileField(validators=[validators.optional()])
    description = StringField(u'Descrição', [
        validators.Required(),
        validators.Length(max=100)])
    value = FloatField('Valor', validators=[
        validators.Required()])
    quantity = IntegerField(u'Quantidade', validators=[
        validators.Required()], widget=NumberInput(min=0))
    unit = StringField('Unidade de Medida', [
        validators.Required(),
        validators.Length(max=2)])
    manufactured = DateField(u'Fabricação', format='%d/%m/%Y')
    validity = DateField(u'Validade', format='%d/%m/%Y')
    submit_product = SubmitField(u'Salvar alterações')

    def fill_provider(self, id):
        provider = Provider.query.get(id)
        if provider:
            self.provider_id.choices = [(provider.id, provider.social_reason)]
            self.provider_id.data = provider.id
            self.provider_id.errors = []


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


class UserForm(FlaskForm):
    name = StringField('Nome', validators=[validators.Required()])
    email = EmailField('E-mail', validators=[
        validators.Required(), validators.Email()])
    password = PasswordField('Senha')
    user_type_id = SelectField(u'Tipo de Usuário', coerce=int, validators=[
        validators.Required()])
    submit_user = SubmitField('Cadastrar')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.user_type_id.choices = [
            (u.id, u.description) for u in UserType.query.all()]
        self.user_type_id.choices.insert(0, (0, ''))
