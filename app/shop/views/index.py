# -*- coding: utf-8 -*-

from flask import render_template
from .. import shop
from ...models import Product


@shop.route('/')
def index():
    products = Product.query.all()
    return render_template('shop/index.html', products=products)
