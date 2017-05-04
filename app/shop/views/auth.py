# -*- coding: utf-8 -*-

from flask import flash, redirect, request, render_template, url_for
from flask_login import (
    current_user, login_required, login_user, logout_user)

from .. import shop
from ..forms import LoginForm, AccountForm
from ... import db
from ...models import User


@shop.route('/login', methods=('GET', 'POST',))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('shop.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('shop.index'))
        flash(u'Usuário ou senha inválidos!')
    return render_template('shop/auth/login.html', form=form)


@shop.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('shop.login'))


@shop.route('/conta/criar', methods=('GET', 'POST',))
def create_account():
    form = AccountForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        user.user_type_id = 2
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('shop.index'))
    return render_template('shop/auth/create_user.html', form=form)
