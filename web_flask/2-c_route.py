#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Defines the web root directory"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """Defines a location for /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_is_fun_page(text=None):
    """Defines a location /c/<text>"""
    parts = text.split('_')
    result = f"C {' '.join(parts)}"
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
