# -*- coding: utf-8 -*-

from flask import Blueprint

admin = Blueprint('admin', __name__)

from .views.city import * #noqa
from .views.product import * #noqa
from .views.provider import * #noqa
from .views.user import * #noqa
