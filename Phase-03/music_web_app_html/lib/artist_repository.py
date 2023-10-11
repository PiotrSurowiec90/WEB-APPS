from lib.artist import Artist
from lib.album import Album

class ArtistRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute("SELECT * from artists")
        artists = []
        for row in rows:
            item = Artist(row["id"], row["name"], row["genre"])
            artists.append(item)
        return artists

    # Find a single artist by their id
    def find(self, artist_id):
        rows = self._connection.execute(
            "SELECT * from artists WHERE id = %s", [artist_id]
        )
        row = rows[0]
        return Artist(row["id"], row["name"], row["genre"])

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, artist):
        self._connection.execute(
            "INSERT INTO artists (name, genre) VALUES (%s, %s)",
            [artist.name, artist.genre],
        )
        return None

    # Delete an artist by their id
    def delete(self, artist_id):
        self._connection.execute("DELETE FROM artists WHERE id = %s", [artist_id])
        return None

    def find_with_albums(self, artist_id):
        query = "SELECT artists.id AS artist_id, artists.name, artists.genre,albums.id AS album_id, albums.title, albums.release_year\
                FROM artists JOIN albums\
                ON artists.id=albums.artist_id WHERE artists.id = %s"
        rows = self._connection.execute(query, [artist_id])
        albums = []
        for row in rows:
            albums.append(
                Album(row.get('album_id'), row.get('title'), row.get('release_year'), row.get('artist_id'))
            )
        return Artist(rows[0].get('artist_id'), rows[0].get('name'), rows[0].get('genre'), albums)