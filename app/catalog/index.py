# -*- coding: utf-8 -*-

from flask import render_template
from . import catalog


@catalog.route('/')
def index():
    return render_template('index.html')
