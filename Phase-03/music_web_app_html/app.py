import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repository import ArtistRepository


# Create a new Flask app
app = Flask(__name__)


# Albums list view.
@app.route("/albums", methods=["GET"])
def albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    albums = repo.all()
    print(albums)
    return render_template("music_library/albums.html", albums=albums)


# Albums detial view
@app.route("/albums/<int:album_id>")
def album_detail(album_id):
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    album = repo.find(album_id)
    return render_template("music_library/album_detail.html", album=album)


@app.route("/artists", methods=["GET"])
def artist_list():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)

    artists = repo.all()
    return render_template("music_library/artist_list.html", artists=artists)


@app.route("/artists/<int:artist_id>", methods=["GET"])
def artist_detail(artist_id):
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)

    artist_obj = repo.find(artist_id)
    return render_template("music_library/artist_detail.html", artist=artist_obj)


@app.route("/albums/create", methods=["GET", "POST"])
def album_create():
    connection = get_flask_database_connection(app)
    album_repo = AlbumRepository(connection)

    if request.method == "GET":
        return render_template("music_library/album_create.html")

    if request.method == "POST":
        new_album = Album(
            None,
            request.form.get("title"),
            request.form.get("release_year"),
            request.form.get("artist_id"),
        )
        if new_album.is_valid():
            new_album = album_repo.create(new_album)
            return redirect(url_for("album_detail", album_id=new_album.id))

        else:
            return render_template(
                "music_library/album_create.html", errors=new_album.generate_errors()
            )


@app.route("/artists/create", methods=["GET", 'POST'])
def artist_create():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)

    if request.method == "GET":
        return render_template("music_library/artist_create.html")

    if request.method == "POST":
        new_artist = Artist(None, request.form.get("name"), request.form.get("genre"))
        if new_artist.is_valid():
            new_artist = repo.create(new_artist)
            return redirect(url_for("artist_detail", artist_id=new_artist.id))
        else:
            return render_template(
                "music_library/artist_create.html", errors=new_artist.generate_errors()
            )


# == Example Code Below ==


# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route("/emoji", methods=["GET"])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template("emoji.html", emoji=":)")


# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes

apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))
