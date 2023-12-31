#!/usr/bin/python3

"""
script that starts a Flask web application listening on 0.0.0.0, port 5000
"""

from flask import Flask
from flask import render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python(text="is cool"):
    """ method return Python """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ method return number """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ method return number template"""
    return render_template('5-number.html', n=n)


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000)
