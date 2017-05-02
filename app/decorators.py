# -*- coding: utf-8 -*-

from functools import wraps
from flask import abort
from flask_login import current_user


def permission_required(*roles):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.has_permission(roles):
                return abort(404)
            return f(*args, **kwargs)
        return wrapped
    return decorator
