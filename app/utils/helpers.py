# -*- coding: utf-8 -*-

from flask import render_template


class MakeShellContext():
    '''
    Creates a callable wrap to flask-script shell

    :param app: application object
    :param db: database ORM instance
    :param models: list of model objects
    '''

    def __init__(self, app, db, *models):
        self._app = app
        self._db = db
        self._models = dict((m.__name__, m) for m in models)

    def __call__(self):
        return dict(app=self._app, db=self._db, **self._models)


class HandleError():
    '''
    Create error pages for flask

    :param template: template to render on error page.
    :param message: error message to be showed.
    '''
    def __init__(self, template, message):
        self.message = message
        self.template = template

    def __call__(self, error):
        '''
        :param error: Error object of errorhandler
        '''
        return render_template(self.template, error=self.message), error.code
