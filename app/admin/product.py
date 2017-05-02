# -*- coding: utf-8 -*-

from flask import current_app, request, render_template, redirect, url_for
from flask_login import login_required

from . import admin
from .forms import ProductForm
from .. import db
from ..models import Product
from ..decorators import permission_required
from ..utils.uploader import upload_image, remove_image


@admin.route('/produtos/')
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
    return render_template('admin/product/index.html', products=products,
                           pagination=pagination)


@admin.route('/produtos/adicionar/', methods=['GET', 'POST'])
@login_required
@permission_required('admin')
def add_product():
    form = ProductForm()
    provider = request.form.get('provider_id', 0, type=int)
    form.fill_provider(provider)

    if form.validate_on_submit():
        product = Product()
        form.populate_obj(product)
        db.session.add(product)
        db.session.commit()
        if form.image_file.data:
            product.image = upload_image('products', form.image_file.data,
                                         product.id)
            db.session.add(product)
            db.session.commit()
        return redirect(url_for('admin.products'))
    return render_template('admin/product/view.html', form=form,
                           label='Adicionar Produto', color='success')


@admin.route('/produtos/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@permission_required('admin')
def edit_product(id):
    product = Product.query.get_or_404(id)
    form = ProductForm(obj=product)
    provider = request.form.get('provider_id', 0, type=int) or \
        product.provider_id
    form.fill_provider(provider)

    if request.method == 'POST' and form.validate():
        form.populate_obj(product)
        if form.image_file.data:
            product.image = upload_image('products', form.image_file.data,
                                         product.id)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('admin.products'))
    return render_template('admin/product/view.html', form=form,
                           label='Editar Produto', color='warning')


@admin.route('/produtos/excluir/<int:id>', methods=['DELETE'])
@login_required
@permission_required('admin')
def delete_product(id):
    product = Product.query.get_or_404(id)
    remove_image(product.image)
    db.session.delete(product)
    db.session.commit()
    return '', 204
