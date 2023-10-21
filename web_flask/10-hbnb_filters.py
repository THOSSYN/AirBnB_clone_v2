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


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays a web page"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    cities = sorted(storage.all(City).values(), key=lambda city: city.name)
    amenities = sorted(storage.all(Amenity).values(),
                       key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
