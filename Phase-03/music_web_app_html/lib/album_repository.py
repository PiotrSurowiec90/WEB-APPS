from lib.album import Album
from lib.artist_repository import ArtistRepository


class AlbumRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        return [Album(**row) for row in rows]

    def find(self, album_id):
        query = "SELECT * FROM albums WHERE id = %s" % album_id
        row = self._connection.execute(query)[0]
        return Album(**row)

    def create(self, new_album):
        query = (
            "INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s) RETURNING id"
        )
        rows = self._connection.execute(
            query, [new_album.title, new_album.release_year, new_album.artist_id]
        )
        new_album.id = rows[0].get('id')
        return new_album
    def delete(self, album_id):
        query = "DELETE FROM albums WHERE id = %s"
        self._connection.execute(query, [album_id])
