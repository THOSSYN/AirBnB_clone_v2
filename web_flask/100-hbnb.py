#!/usr/bin/python3
"""Starts a flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_method(exception):
    """A method that removes the current sqlalchemy"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """Displays a web page"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    cities = sorted(storage.all(City).values(), key=lambda c: c.name)
    places = sorted(storage.all(Place).values(), key=lambda p: p.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda a: a.name)
    return render_template('100-hbnb.html', states=states,
                           cities=cities, amenities=amenities, places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
