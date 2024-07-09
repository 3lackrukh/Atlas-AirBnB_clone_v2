#!/usr/bin/python3
""" This module defines a web application"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ Display HTML page"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    for state in states:
        state.cities.sort(key=lambda city: city.name)
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('10-hbnb_filters.html', states=sorted_states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
