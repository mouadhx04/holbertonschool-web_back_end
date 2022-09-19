#!/usr/bin/env python3
""" a basic flask app"""
from datetime import datetime
from flask import Flask, g, render_template, request
from flask_babel import Babel, _, format_datetime
import pytz

app = Flask(__name__)


class Config(object):
    """ Config class for Babel object """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    """ function to determine if a user is logged in, and the language """
    id = request.args.get('login_as')
    d_user = get_user(id)
    if d_user:
        g.user = d_user


def get_user(id):
    """ returns a user dictionary or None """
    if id and int(id) in users:
        return users[int(id)]
    return None


@app.route('/')
def hello():
    """ render a basic html file """
    login = False
    if g.get('user') is not None:
        login = True
    current_t = format_datetime(datetime.now())
    return render_template('index.html', login=login, current_time=current_t)


@babel.localeselector
def get_locale() -> str:
    """ a function to determine the best match with the supported languages """
    lg = request.args.get('locale')
    if lg in app.config['LANGUAGES']:
        return lg
    if (g.get('user') and g.user.get("locale", None)
            and g.user["locale"] in app.config['LANGUAGES']):
        return g.user["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    "returns the timezone"
    try:
        if request.args.get('timezone'):
            return str(pytz.timezone(request.args.get('timezone')))
        if g.get('user') and g.user.get('timezone'):
            return str(pytz.timezone(g.user['timezone']))
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return app.config["BABEL_DEFAULT_TIMEZONE"]


if __name__ == '__main__':
    app.run()
