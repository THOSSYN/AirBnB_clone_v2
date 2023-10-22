#!/usr/bin/python3
"""A script that starts a flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """Removes a session after each request"""
    storage.close()


"""@app.route('/states', strict_slashes=False)
def states_list():
    Displays a list of state
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_list_by_id(id):
    Displays a list of state
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')"""
@app.route('/states', strict_slashes=False)
def states_list():
    """Displays a list of state"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('index.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """Displays a list of state"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('index.html', states=states, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
