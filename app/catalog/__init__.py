# -*- coding: utf-8 -*-

from flask import Blueprint

catalog = Blueprint('catalog', __name__)

from .auth import * #noqa
from .index import * #noqa
