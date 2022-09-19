#!/usr/bin/env python3
""" a basic flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config(object):
    """ Config class for Babel object """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def hello():
    """ render a basic html file """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """ a function to determine the best match with the supported languages """
    if request.full_path.split('/')[1][:8] == "?locale=":
        lg = request.full_path.split('/')[1][8:]
        if lg in app.config['LANGUAGES']:
            return lg
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
