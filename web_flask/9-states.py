#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.config['ERROR_INCLUDE_HTML'] = False


@app.teardown_appcontext
def teardown_session(exception):
    """
    Removes the current SQLAlchemy Session
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """
    Displays a HTML page with a list of all State objects sorted by name
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """
    Displays a HTML page with a list of City objects linked to a State
    sorted by name
    """
    state = storage.get(State, id)
    if state is None:
        return (
            """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <title>HBNB</title>
            </head>
            <body>
                <h1>Not found!</h1>
            </body>
            </html>
            """,
            404
        )
    else:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('9-states.html', state=state, cities=cities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
