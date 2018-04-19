#!/usr/bin/python3
'''
    Starts a Flask web application
    listens on 0.0.0.0, port 5000
    Uses storage for fetching data
    from storage engine
'''
from flask import Flask, render_template
import models
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''Renders an HTML page with a list of states'''
    states = models.storage.all(models.classes["State"])
    print(states)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def storage_close(exception):
    '''Closes a session of storage'''
    models.storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
