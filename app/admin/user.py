# -*- coding: utf-8 -*-

from flask import current_app, request, render_template, redirect, url_for
from flask_login import login_required

from . import admin
from .forms import UserForm
from .. import db
from ..models import User
from ..decorators import permission_required


@admin.route('/usuarios/')
@login_required
@permission_required('admin')
def users():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search')
    filters = ()
    if search:
        filters += (User.name.like('%'+search+'%'),)
    pagination = User.query.filter(*filters).order_by(
        User.name.asc()).paginate(
            page, per_page=current_app.config['PER_PAGE'], error_out=False)
    users = pagination.items
    return render_template('admin/user/index.html', users=users,
                           pagination=pagination)


@admin.route('/usuarios/adicionar/', methods=['GET', 'POST'])
@login_required
@permission_required('admin')
def add_user():
    form = UserForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('admin.users'))
    return render_template('admin/user/view.html', form=form,
                           label='Adicionar usuario', color='success')


@admin.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@permission_required('admin')
def edit_user(id):
    user = User.query.get_or_404(id)
    form = UserForm(request.form, obj=user)

    if request.method == 'POST' and form.validate():
        form.populate_obj(user)
        if form.password.data == '':
            user.password_hash = User.query.get(id).password_hash
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('admin.users'))
    return render_template('admin/user/view.html', form=form,
                           label='Editar usuario', color='warning')


@admin.route('/usuarios/excluir/<int:id>', methods=['DELETE'])
@login_required
@permission_required('admin')
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204
