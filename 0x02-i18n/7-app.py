#!/usr/bin/env python3
"""Task 7: Infer the appropriate timezone"""
from typing import Dict, Union

import pytz
from flask import Flask, g, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Find a user using ID"""
    login_as = request.args.get("login_as")
    if not login_as or int(login_as) not in users:
        return None
    return users.get(int(login_as))


@app.before_request
def before_request() -> None:
    """Check login user"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Finds the best matching language"""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone() -> str:
    """use the appropriate timezone"""
    time_zone = request.args.get("timezone", None)
    if time_zone is None and g.user:
        time_zone = g.user["timezone"]
    try:
        return pytz.timezone(time_zone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return "UTC"


@app.route("/")
def index() -> str:
    """Entry point route"""
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run()
