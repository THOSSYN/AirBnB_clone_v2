#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask, abort, render_template

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
def C_is_fun_page(text="is cool"):
    """Defines a location /c/<text>"""
    parts = text.split('_')
    result = f"C {' '.join(parts)}"
    return result


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Py_is_magic_page(text="is cool"):
    """Defines a location /python/<text>"""
    if text:
        parts = text.split('_')
        result = f"Python {' '.join(parts)}"
        return result


@app.route('/number/<n>', strict_slashes=False)
def number_route(n):
    """Displays n is number if n is int"""
    try:
        n = int(n)
        return f"{n} is a number"
    except Exception as e:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def number_html_route(n):
    """Displays an html page if n is an int"""
    try:
        n = int(n)
        return render_template('5-number.html', n=n)
    except Exception as e:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
