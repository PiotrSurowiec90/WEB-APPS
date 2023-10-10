from lib.base_model_manager import BaseModelManager
from lib.album import Album


class AlbumRepository(BaseModelManager):
    def __init__(self, connection) -> None:
        super().__init__(connection)
        self._model_class = Album
        self._table_name = "albums"

    def create(self, new_album):
        query = (
            ""
            "INSERT INTO albums (title, release_year, artist_id)"
            "VALUES (%s, %s, %s)"
        )
        self._connection.execute(
            query, [new_album.title, new_album.release_year, new_album.artist_id]
        )
        return None
