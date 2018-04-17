#!/usr/bin/python3
'''
    Starts a Flask web application and
    routes /, /hbnb, /c/, /python/,
    /number/, and /number_template/ urls
    Renders a jinja template if n is an int
'''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Routes 'Hello HBNB!' to index'''
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Routes 'HBNB!' to /hbnb'''
    return 'HBNB!'

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    '''Returns 'C ' + user input'''
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    '''Returns 'Python ' + user input & defaults to (Python is cool)'''
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<n>', strict_slashes=False)
def is_number(n):
    '''Displays 'n is a number' if it is an int'''
    if n.isdigit():
        return '{} is a number'.format(n)

@app.route('/number_template/<n>', strict_slashes=False)
def num_template(n):
    '''Displays an HTML page if n is an int'''
    if n.isdigit():
        return render_template('5-number.html', n=n)

if __name__=='__main__':
    app.run(host= '0.0.0.0', port=5000)
