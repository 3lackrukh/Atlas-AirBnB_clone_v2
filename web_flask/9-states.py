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


@app.route("/states", strict_slashes=False)
def render_states():
    """renders states from db to route /states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route("/states/<id>", strict_slashes=False)
def render_states_id(id):
    """renders state.id from db to route /states/<id>"""
    states = storage.all(State).values()
    selected_state = "not found!"
    for state in states:
        if str(state.id) == id:
            selected_state = state
            selected_state.cities.sort(key=lambda city: city.name)
            break
    return render_template("9-states.html", state=selected_state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
