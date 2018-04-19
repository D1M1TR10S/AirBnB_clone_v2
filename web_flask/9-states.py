#!/usr/bin/python3
'''
    Starts a Flask web application
    listens on 0.0.0.0, port 5000
    Lists all states or state matching
    id passed as an arg
'''
from flask import Flask, render_template
import models
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<input_id>', strict_slashes=False)
def states_state(input_id=''):
    '''Renders an HTML page with the state matching id'''
    cities = models.storage.all(models.classes["City"])
    states = models.storage.all(models.classes["State"])
    exists = 0
    for k, v in states.items():
        if input_id == v.id:
            exists = 1
    return render_template('9-states.html',
                           states=states, cities=cities,
                           input_id=input_id, exists=exists)

@app.teardown_appcontext
def storage_close(exception):
    '''Closes a session of storage'''
    models.storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
