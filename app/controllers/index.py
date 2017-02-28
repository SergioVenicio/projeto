# -*- coding: utf-8 -*-

from flask import render_template
from . import controller


@controller.route('/')
def index():
    return render_template('index.html')
