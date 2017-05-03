# -*- coding: utf-8 -*-

import os
import magic
from time import strftime
from flask import current_app, url_for


def upload_image(folder, file, name):
    extension = magic.from_buffer(file.read(1024), mime=True).split('/')[1]
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


def remove_image(image):
    folder = current_app.config['UPLOAD_FOLDER']
    image = image.replace(os.path.join(os.sep, 'static', 'uploads', ''), '')
    image = os.path.join(folder, image)
    path_day = os.path.dirname(image)
    path_month = os.path.abspath(os.path.join(path_day, os.pardir))
    try:
        if os.path.isfile(image):
            os.remove(image)
        if not os.listdir(path_day):
            os.rmdir(path_day)
        if not os.listdir(path_month):
            os.rmdir(path_month)
    except:
        pass
