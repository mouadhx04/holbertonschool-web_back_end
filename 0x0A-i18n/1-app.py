#!/usr/bin/env python3
'''
flask application
'''

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    ''' Config Class'''
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
Babel.default_locale = 'en'
Babel.default_timezone = 'UTC'


@app.route('/')
def index():
    '''0-index.html.'''
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run()
