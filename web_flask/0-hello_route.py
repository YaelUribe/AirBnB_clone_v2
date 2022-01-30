#!/usr/bin/python3
"""Script: hello_route
    starts a new Flask app"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    return "Hello, HBNB!"
