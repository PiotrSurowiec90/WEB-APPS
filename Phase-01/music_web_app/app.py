import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
# Create a new Flask app
app = Flask(__name__)


"""@app.route("/albums", methods = ['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    albums = repo.all()
    return '\n'.join([f"{album}" for album in albums])"""

# == Your Routes Here ==
@app.route("/albums", methods = ['POST', 'GET'])
def albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    if request.method == 'POST':
        new_album = Album(None, **request.form)
        repo.create(new_album)
        return "Album created!"
    
    albums = repo.all()
    return '\n'.join([f"{album}" for album in albums])

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

