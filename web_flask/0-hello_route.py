#!/usr/bin/python3
"""This module defines the web application hello_hbnb"""

from flask import Flask


app = Flask(__name__)

""" App routing and method definition"""
@app.route('/', strict_slashes=False)
def hello_hbnb ():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run (host='0.0.0.0', port=5000)
