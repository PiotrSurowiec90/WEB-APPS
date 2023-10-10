from lib.base_model_manager import BaseModelManager
from lib.artist import Artist


class ArtistRepository(BaseModelManager):
    def __init__(self, connection) -> None:
        super().__init__(connection)
        self._model_class = Artist
        self._table_name = "artists"

    def create(self, new_artist):
        query = "INSERT INTO artists (name, genre) VALUES (%s, %s)"
        self._connection.execute(query, [new_artist.name, new_artist.genre])
        return None
