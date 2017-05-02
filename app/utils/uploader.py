# -*- coding: utf-8 -*-

import os
import imghdr
from time import strftime
from flask import current_app, url_for


def upload_image(folder, file, name):
    print(name)
    extension = imghdr.what('', file.read())
    file.seek(0)
    config = current_app.config
    if extension in config['ALLOWED_EXTENSIONS']:
        month_day = os.path.join(strftime('%m'), strftime('%d'))
        folderpath = os.path.join(config['UPLOAD_FOLDER'], folder, month_day)
        if not os.path.isdir(folderpath):
            os.makedirs(folderpath)
        filename = '{}.{}'.format(name, extension)
        filepath = os.path.join(folderpath, filename)
        file.save(filepath)
        return url_for('static', filename=os.path.join(
            'uploads', folder, month_day, filename))
    else:
        return None


def remove_image(path):
    folder = current_app.config['UPLOAD_FOLDER']
    path = path.replace(os.path.join(os.sep, 'static', 'uploads', ''), '')
    path = os.path.join(folder, path)
    if os.path.isfile(path):
        try:
            os.remove(path)
        except:
            pass
