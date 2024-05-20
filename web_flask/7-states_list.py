#!/usr/bin/python3
"""
This Flask web application provides a list of states retrieved from a database
using an ORM (Object-Relational Mapper). Users can access the sorted list at
the `/states_list` endpoint.

The application renders an HTML template (`7-states_list.html`) to display
the state names.

**Functionalities:**

* Retrieves all `State` objects from the database using the `storage` object.
* Sorts the retrieved states alphabetically by their `name` attribute.
* Renders the `7-states_list.html` template passing the sorted list of states.

**Database and ORM:**

This application interacts with a database likely through an
ORM (Object-Relational Mapper) indicated by the usage of `storage` and `State`
class from the `models` module.

**Error Handling:**

The `teardown_appcontext` function ensures the database connection is properly
closed after each request, preventing potential issues.
"""

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
