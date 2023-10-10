import os
from flask import Flask, request

from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)


# == Your Routes Here ==
@app.route("/albums", methods=["POST", "GET"])
def albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    if request.method == "GET":
        albums = repo.all()
        return "\n".join([f"{album}" for album in albums])

    if request.form:
        new_album = Album(None, **request.form)
        repo.create(new_album)
        return "Album created!"
    else:
        return "Invalid data"


@app.route("/artists", methods=["GET", "POST"])
def artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    if request.method == 'GET':
        artists = repo.all()
        return ", ".join([str(artist) for artist in artists])
    
    if request.form:
        new_artist = Artist(None, **request.form)
        repo.create(new_artist)
        return '', 200

    return "Form data is invalid!", 400




# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))
