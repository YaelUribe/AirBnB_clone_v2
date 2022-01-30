#!/usr/bin/python3
"""
    starts a new Flask app
"""
from flask import Flask, render_template, template_rendered
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_1(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run()
