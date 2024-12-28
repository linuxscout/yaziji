#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os

from flask import Flask, request, jsonify
from flask_cors import cross_origin
from flask_babel import Babel, force_locale
import locale

# from config.yaziji_config import config_factory
# import adaat
from data import data_const


# Ensure UTF-8 encoding for output
if locale.getpreferredencoding().upper() != 'UTF-8':
    locale.setlocale(locale.LC_ALL, 'ar_DZ.UTF-8')


# Configure the Flask app
app = Flask(__name__, static_url_path='/static', static_folder='static')
# Create a Babel instance for our app
babel = Babel(app)
babel.init_app(app)

@app.route("/selectGet", methods=["POST", "GET"])
@app.route("/<lang>/selectGet", methods=["POST", "GET"])
@cross_origin()
def selectget(lang="ar"):
    """
    Example of using AJAX/JSON for select values.
    """
    with force_locale(lang):
        return jsonify(data_const.selectValues)

if __name__ == "__main__":
    app.run(debug=True)
