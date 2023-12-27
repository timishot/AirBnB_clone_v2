#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    n_text = text.replace("_", " ")
    return f"C {n_text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    n_text = text.replace("_", " ")
    return f"Python {n_text}"


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
