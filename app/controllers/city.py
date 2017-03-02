#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, current_app, jsonify, request
from flask_login import login_required
from . import controller
from ..models import City


@controller.route('/cidades/')
@login_required
def cities():
    if not request.is_xhr:
        abort(404)
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search')
    filters = ()
    if search:
        filters += (City.description.like('%'+search+'%'),)
    pagination = City.query.filter(*filters).order_by(
        City.description.asc()).paginate(
            page, per_page=current_app.config['PER_PAGE'], error_out=False)
    cities = pagination.items
    return jsonify({
        'cities': [{
            'id': c.id,
            'description': c.description,
            'state': c.state.acronym,
        } for c in cities]
    })
