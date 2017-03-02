# -*- coding: utf-8 -*-

from flask import current_app, request, render_template, redirect, url_for
from flask_login import login_required
from . import controller
from .. import db
from ..models import Product, Provider
from ..forms.products import ProductForm
from ..decorators.permission import permission_required


@controller.route('/produtos/')
@login_required
@permission_required('admin')
def products():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search')
    filters = ()
    if search:
        filters += (Product.description.like('%'+search+'%'),)
    pagination = Product.query.filter(*filters).order_by(
        Product.description.asc()).paginate(
            page, per_page=current_app.config['PER_PAGE'], error_out=False)
    products = pagination.items
    return render_template('product/index.html', products=products,
                           pagination=pagination)


@controller.route('/produtos/adicionar/', methods=['GET', 'POST'])
@login_required
@permission_required('admin')
def add_product():
    form = ProductForm()
    provider = request.form.get('provider_id', 0, type=int)

    if provider:
        provider = Provider.query.get(provider)
        form.provider_id.choices = [(provider.id, provider.social_reason)]
        form.provider_id.data = provider.id
        form.provider_id.errors = []

    if request.method == 'POST' and form.validate_on_submit():
        product = Product()
        form.populate_obj(product)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('controller.products'))
    return render_template('product/view.html', form=form,
                           label='Adicionar Produto', color='success')


@controller.route('/produtos/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@permission_required('admin')
def edit_product(id):
    product = Product.query.get_or_404(id)
    provider = product.provider
    new_provider = request.form.get('provider_id', 0, type=int)
    form = ProductForm(request.form, obj=product)
    form.provider_id.choices = [(provider.id, provider.social_reason)]

    if new_provider:
        provider = Provider.query.get(new_provider)
        form.provider_id.choices = [(provider.id, provider.social_reason)]
        form.provider_id.data = provider.id
        form.provider_id.errors = []

    if request.method == 'POST' and form.validate():
        form.populate_obj(product)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('controller.products'))
    return render_template('product/view.html', form=form,
                           label='Editar Produto', color='warning')


@controller.route('/produtos/excluir/<int:id>', methods=['DELETE'])
@login_required
@permission_required('admin')
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return '', 204
