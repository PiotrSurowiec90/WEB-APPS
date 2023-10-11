from lib.album import Album
from lib.album_repository import AlbumRepository


'''def test_get_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    album_repo = AlbumRepository(db_connection)
    albums = album_repo.all()
    assert albums[:3] == [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
    ]


def test_find(db_connection):
    db_connection.seed("seeds/music_library.sql")
    album_repo = AlbumRepository(db_connection)
    result = album_repo.find(1)
    assert result == Album(1, "Doolittle", 1989, 1)


def test_create(db_connection):
    db_connection.seed("seeds/music_library.sql")
    album_repo = AlbumRepository(db_connection)
    new_album = Album(None, 'Title', 2023, 1)
    album_repo.create(new_album)
    result = album_repo.find(13)
    expected = Album(13, 'Title', 2023, 1)
    assert result == expected

def test_delete(db_connection):
    db_connection.seed("seeds/music_library.sql")
    album_repo = AlbumRepository(db_connection)
    album_repo.delete(1)
    result = album_repo.all()[:2]
    expected = [
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
    ]
    assert result == expected'''

