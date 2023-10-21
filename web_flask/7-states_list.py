#!/usr/bin/python3
"""A script that starts a flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Removes a session after each request"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_route():
    """Displays a list of state"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
