# -*- coding: utf-8 -*-

from flask import flash, redirect, request, render_template, url_for
from flask_login import (
    current_user, login_required, login_user, logout_user)
from ..forms.login import LoginForm
from ..models.users import User
from . import controller


@controller.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('controller.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or
                            url_for('controller.index'))
        flash(u'Usuário ou senha inválidos!')
    return render_template('auth/login.html', form=form)


@controller.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('controller.login'))
