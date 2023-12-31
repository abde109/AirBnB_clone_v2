#!/usr/bin/python3

"""
script that starts a Flask web application listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def route():
    """ method return Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ method return HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """ method return C """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
def Python(text="is cool"):
    """ method return Python """
    return 'Python {}'.format(text.replace('_', ' '))


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000)
