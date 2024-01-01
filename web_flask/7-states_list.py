#!/usr/bin/python3
"""
script that starts a Flask web application listening on 5000
"""

from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ method returns states_list """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states.values())


@app.teardown_appcontext
def teardown_db(exception):
    """ method to remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
