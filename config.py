# -*- coding: utf-8 -*-

import os
import random

basedir = os.path.abspath(os.path.dirname('__file__'))


def generate_key(length):
    '''
    Generate random key with a fixed length

    :param length: string length to be generated
    '''
    seed = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            '0123456789!@#$%^&*({-_=+})')
    return ''.join([random.choice(seed) for s in range(length)])


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or generate_key(64)
    PER_PAGE = 2
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class Development(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'storage-dev.db')
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


class Production(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'storage.db')
    DEBUG = False
