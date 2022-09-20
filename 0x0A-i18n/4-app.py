#!/usr/bin/env python3
"""second app"""
from flask import Flask, render_template
from flask_babel import Babel
from flask import g, request


app = Flask(__name__)
# app.config.from_pyfile('babel.cfg')
babel = Babel(app)


class Config:
    """ config class"""
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """get locale function"""
    f = request.args.get('locale')
    if f:
        return f
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """route function"""
    return render_template("4-index.html")


if __name__ == '__main__':
    app.run()
