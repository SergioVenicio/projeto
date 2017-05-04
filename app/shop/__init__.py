# -*- coding: utf-8 -*-

from flask import Blueprint

shop = Blueprint('shop', __name__)

from .views.auth import * # noqa
from .views.index import * # noqa
