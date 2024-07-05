#!/usr/bin/python3
"""This module defines the web application hello_hbnb"""

from flask import Flask

app = Flask(__name__)

""" App routing and method definition"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C {}'.format(text.replace('_', ' '))
# replace underscore with space


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))
# displays Python followed by input text
# replace underscore with space


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'

""" Run the app"""
# runs the app in debug mode
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
