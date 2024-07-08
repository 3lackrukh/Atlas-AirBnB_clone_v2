#!/usr/bin/python3
""" this module defines a web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ closes the storage """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """ returns a list of cities by state """
    states = storage.all(State).values()
    for state in states:
        state.cities.sort(key=lambda city: city.name)
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
