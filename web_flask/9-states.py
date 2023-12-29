#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
"to display 7-states_list.html"
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States.
    States are sorted by name.
    """
    states = storage.all(State)
    return render_template("9-states.html", state=states)

@app.route("/states/<id>", strict_slashes=False)
def cities(id=None):
    """Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state= state)
        return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
