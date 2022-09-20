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
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    '''determine the best match with our supported languages.'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
