# -*- config: utf-8 -*-

from flask import Blueprint

controller = Blueprint('controller', __name__)

from .auth import * # noqa
from .index import * # noqa
