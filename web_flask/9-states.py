#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """ method returns states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ method returns states by id """
    states = storage.all(State).values()
    state = next((s for s in states if s.id == id), None)
    return render_template('9-states.html', states=states, id=id, state=state)


@app.teardown_appcontext
def close_db(exception):
    """ method to remove the current SQLAlchemy Session """
    storage.close()


app.run(host='0.0.0.0', port='5000')
