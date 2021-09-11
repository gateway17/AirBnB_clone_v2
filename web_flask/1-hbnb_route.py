#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_HBT():
    """Returns Hello HBNG! """
    return("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display “HBNB """
    return("HBNB")
