#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Teardown the app context and close the storage session.

    This function is automatically called after each request to ensure that
    the current SQLAlchemy session is properly removed, preventing potential
    issues with database connections.

    :param exception: An exception instance if
    one was raised during the request
    """

    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Display a list of states sorted by name.

    This route retrieves all State objects from storage, sorts them by their
    name attribute, and renders the '7-states_list.html' template to display
    the sorted list of states.

    :return: Rendered HTML template displaying the sorted list of states.
    """

    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
