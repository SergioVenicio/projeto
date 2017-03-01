# -*- coding: utf-8 -*-

from flask import current_app, request, render_template, redirect, url_for
from flask_login import login_required
from . import controller
from .. import db
from ..models import Provider, City
from ..forms.providers import ProviderForm


@controller.route('/fornecedores/')
@login_required
def providers():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search')
    filters = ()
    if search:
        filters += (Provider.social_reason.like('%'+search+'%'),)
    pagination = Provider.query.filter(*filters).order_by(
        Provider.social_reason.asc()).paginate(
            page, per_page=current_app.config['PER_PAGE'], error_out=False)
    providers = pagination.items
    return render_template('provider/index.html', providers=providers,
                           pagination=pagination)


@controller.route('/fornecedores/adicionar/', methods=['GET', 'POST'])
@login_required
def add_provider():
    form = ProviderForm()
    city = request.form.get('city_id', 0, type=int)

    if city:
        city = City.query.get(city)
        form.city_id.choices = [(city.id, city.description)]
        form.city_id.data = city.id
        form.city_id.errors = []

    if request.method == 'POST' and form.validate_on_submit():
        provider = Provider()
        form.populate_obj(provider)
        db.session.add(provider)
        db.session.commit()
        return redirect(url_for('controller.providers'))
    return render_template('provider/view.html', form=form,
                           label='Adicionar Fornecedor', color='success')


@controller.route('/fornecedores/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_provider(id):
    provider = Provider.query.get_or_404(id)
    city = provider.city
    new_city = request.form.get('city_id', 0, type=int)
    form = ProviderForm(request.form, obj=provider)
    form.city_id.choices = [(
        city.id, '{} - {}'.format(city.description, city.state.acronym))]

    if new_city:
        city = City.query.get(new_city)
        form.city_id.choices = [(city.id, city.description)]
        form.city_id.data = city.id
        form.city_id.errors = []

    if request.method == 'POST' and form.validate():
        form.populate_obj(provider)
        db.session.add(provider)
        db.session.commit()
        return redirect(url_for('controller.providers'))
    return render_template('provider/view.html', form=form,
                           label='Editar Fornecedor', color='warning')


@controller.route('/fornecedores/excluir/<int:id>', methods=['DELETE'])
@login_required
def delete_provider(id):
    return '', 204
