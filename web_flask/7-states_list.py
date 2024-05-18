#!/usr/bin/python3
"""
Script to start a Flask web application
"""
import os  # noqa 184
from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy import create_engine

app = Flask(__name__)


def import_sql_dump(dump_path):
    """
    Import SQL dump to have some data
    """
    # Set your database URL (replace with actual credentials and database name)
    database_url = ('mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@'
                    'localhost/hbnb_dev_db')

    # Create an engine to the database
    engine = create_engine(database_url)

    with engine.connect() as connection:
        with open(dump_path, 'r') as file:
            sql_commands = file.read()
            connection.execute(sql_commands)


# Import the SQL dump data
import_sql_dump('7-dump.sql')


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Display a list of states
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
