#!/usr/bin/python3
'''
    Starts a Flask web application and
    routes the index as well as /hbnb
'''
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return 'HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
