#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask


# Create a Flask application
app = Flask(__name__)


# Define a route for the root path
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


# Define a route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


# Run the application on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
