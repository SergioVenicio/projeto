# -*- coding: utf-8 -*-

from flask import Blueprint

shop = Blueprint('shop', __name__)

from .auth import * # noqa
from .index import * # noqa
