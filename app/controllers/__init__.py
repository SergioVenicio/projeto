# -*- config: utf-8 -*-

from flask import Blueprint

controller = Blueprint('controller', __name__)

from .auth import * # noqa
from .index import * # noqa
from .provider import * # noqa
from .city import * # noqa
from .product import * # noqa
