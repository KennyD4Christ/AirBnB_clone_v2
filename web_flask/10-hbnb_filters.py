#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City  # noqa 184
from models.amenity import Amenity

app = Flask(__name__)
app.config['ERROR_INCLUDE_HTML'] = False


@app.teardown_appcontext
def teardown_session(exception):
    """
    Removes the current SQLAlchemy Session
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Displays a HTML page with States, Cities, and Amenities
    """
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
