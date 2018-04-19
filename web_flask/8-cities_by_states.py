#!/usr/bin/python3
'''
    Starts a Flask web application
    listens on 0.0.0.0, port 5000
    Uses storage for fetching data
    from storage engine
    Lists all cities by their state
'''
from flask import Flask, render_template
import models
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    '''Renders an HTML page with a list of cities by their states'''
    cities = models.storage.all(models.classes["City"])
    states = models.storage.all(models.classes["State"])
    return render_template('8-cities_by_states.html'
                           states=states, cities=cities)


@app.teardown_appcontext
def storage_close(exception):
    '''Closes a session of storage'''
    models.storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
