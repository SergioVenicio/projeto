# -*- coding: utf-8 -*-

from flask import (current_app, jsonify, request,
                   render_template, redirect, url_for)
from flask_login import login_required

from . import admin
from .forms import ProviderForm
from .. import db
from ..decorators.permission import permission_required
from ..models import Provider


@admin.route('/fornecedores/')
@login_required
@permission_required('admin')
def providers():
    page = request.args.get('page', 1, type=int)
    xhr = request.args.get('xhr', False, type=bool)
    search = request.args.get('search')
    filters = ()
    if search:
        filters += (Provider.social_reason.like('%'+search+'%'),)
    pagination = Provider.query.filter(*filters).order_by(
        Provider.social_reason.asc()).paginate(
            page, per_page=current_app.config['PER_PAGE'], error_out=False)
    providers = pagination.items
    if xhr and request.is_xhr:
        return jsonify({
            'providers': [{
                'id': p.id, 'social_reason': p.social_reason
            } for p in providers]
        })
    return render_template('provider/index.html', providers=providers,
                           pagination=pagination)


@admin.route('/fornecedores/adicionar/', methods=['GET', 'POST'])
@login_required
@permission_required('admin')
def add_provider():
    form = ProviderForm()
    city = request.form.get('city_id', 0, type=int)
    form.fill_city(city)

    if request.method == 'POST' and form.validate_on_submit():
        provider = Provider()
        form.populate_obj(provider)
        db.session.add(provider)
        db.session.commit()
        return redirect(url_for('admin.providers'))
    return render_template('provider/view.html', form=form,
                           label='Adicionar Fornecedor', color='success')


@admin.route('/fornecedores/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@permission_required('admin')
def edit_provider(id):
    provider = Provider.query.get_or_404(id)
    city = request.form.get('city_id', 0, type=int)
    form = ProviderForm(request.form, obj=provider)

    if city:
        form.fill_city(city)
    else:
        city = provider.city
        form.city_id.choices = [(
            city.id, '{} - {}'.format(city.description, city.state.acronym))]

    if request.method == 'POST' and form.validate():
        form.populate_obj(provider)
        db.session.add(provider)
        db.session.commit()
        return redirect(url_for('admin.providers'))
    return render_template('provider/view.html', form=form,
                           label='Editar Fornecedor', color='warning')


@admin.route('/fornecedores/excluir/<int:id>', methods=['DELETE'])
@login_required
@permission_required('admin')
def delete_provider(id):
    provider = Provider.query.get_or_404(id)
    db.session.delete(provider)
    db.session.commit()
    return '', 204
