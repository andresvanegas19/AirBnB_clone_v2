#!/usr/bin/python3
""" An application server """

from flask import Flask, render_template
from models import storage
from models import *


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(self):
    """ This function provide a method to close an session of
    the storage"""
    storage.close()


@app.route('/hbnb')
def local():
    """ an simply routing to display a list of the state """
    amenities = []
    places = []
    users = []
    for clase in storage.all().values():
        if clase.__class__.__name__ == 'Amenity':
            amenities.append(clase)
        if clase.__class__.__name__ == 'Place':
            places.append(clase)
        if clase.__class__.__name__ == 'User':
            users.append(clase)

    return render_template('10-hbnb_filters.html',
                           states=storage.all('State').values(),
                           cities=storage.all('City').values(),
                           amenities=amenities,
                           places=places,
                           users=users)


if __name__ == '__main__':
    app.run()
