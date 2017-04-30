# -*- coding: utf-8 -*-

from flask import Blueprint

admin = Blueprint('admin', __name__)

from .city import * #noqa
from .product import * #noqa
from .provider import * #noqa
from .user import * #noqa
