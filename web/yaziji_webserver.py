#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, send_from_directory, request, jsonify
from flask_minify import minify
from flask_cors import cross_origin
from flask_babel import Babel, force_locale
import locale

# Local libraries
sys.path.append(os.path.join(os.path.dirname(__file__), "./lib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../yaziji"))

from config.yaziji_config import config_factory
import adaat
from data import data_const


# Ensure UTF-8 encoding for output
if locale.getpreferredencoding().upper() != 'UTF-8':
    locale.setlocale(locale.LC_ALL, 'ar_DZ.UTF-8')

# Load configuration
mywebconfig = config_factory.facory()

# Set up logging based on the debug mode in configuration
if mywebconfig.MODE_DEBUG:
    try:
        my_handler = RotatingFileHandler(
            mywebconfig.LOGGING_FILE, mode='a', maxBytes=5 * 1024 * 1024,
            backupCount=2, encoding=None, delay=0
        )
    except PermissionError:
        print(__file__, "You may verify the log file permissions")
    else:
        logging.basicConfig(level=logging.DEBUG, handlers=[my_handler])
else:
    logging.basicConfig(filename=mywebconfig.LOGGING_FILE, level=logging.INFO)

# Configure the Flask app
app = Flask(__name__, static_url_path='/static', static_folder='static')
minify(app=app, html=True, js=True, cssless=True)

app.config.from_object(mywebconfig)

# Create a Babel instance for our app
babel = Babel(app)


def get_locale():
    """Extract language from URL path."""
    language = request.path.split('/')[1]
    if language in app.config['BABEL_LANGUAGES']:
        return language
    return app.config['BABEL_DEFAULT_LOCALE']


babel.init_app(app)


@app.route("/index/")
def index():
    return render_template("index.html", current_page='index')



@app.route("/")
@app.route("/<lang>/")
def home(lang="ar"):
    context = {}
    available_languages = app.config['BABEL_LANGUAGES']
    url_host_path = app.config['URL_HOST_PATH']
    with force_locale(lang):  # Set the locale
        return render_template(
            "index.html", current_page='home',
            available_languages=available_languages,
            url_host_path=url_host_path, **context
        )


@app.route("/ajaxGet", methods=["POST", "GET"])
@app.route("/<lang>/ajaxGet", methods=["POST", "GET"])
@cross_origin()
def ajax(lang="ar"):
    """
    Handle AJAX requests for various actions.
    """
    default = ""
    args = request.args if request.method == "GET" else request.get_json(silent=True).get("data", {})

    if args.get("response_type", "") == "get_random_text":
        return jsonify({"text": default})

    text = args.get("text", "")
    action = args.get("action", "")
    # remove "text" and "action" if from options
    options = {key: value for key, value in dict(request.args).items() if key not in ["text","action"]}
    myadaat = adaat.Adaat()  # Instantiate the Adaat class
    resulttext = myadaat.do_action(text, action, options)

    return jsonify({'result': resulttext, 'order': 0})


@app.route("/selectGet", methods=["POST", "GET"])
@app.route("/<lang>/selectGet", methods=["POST", "GET"])
@cross_origin()
def selectget(lang="ar"):
    """
    Example of using AJAX/JSON for select values.
    """
    with force_locale(lang):
        return jsonify(data_const.selectValues)


@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("result.html", result=result)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


@app.route('/<lang>/static', methods=['GET'])
def lang_static():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == "__main__":
    app.run(debug=True)
