# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname('__file__'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        'W@5aGtIok&*%2346aU!cA$LxF#9667+EcJlM'
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class Development(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'storage-dev.db')
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


class Production(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'storage.db')
    DEBUG = False
