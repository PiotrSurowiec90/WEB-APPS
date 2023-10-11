from lib.album import Album


def test_album_init():
    # Test new instance has correct attrs.
    new_album = Album(
        1,
        'Title',
        2018,
        1
    )
    assert new_album.id == 1
    assert new_album.title == 'Title'
    assert new_album.release_year == 2018
    assert new_album.artist_id == 1

def test_repr_artist():
    # Test representation of the class.
    new_album = Album(
        1,
        'Title',
        2018,
        1
    )
    assert str(new_album) == "Title, 2018"


def test_two_albums_same_data():
    # Test two instances with the same data are equal.
    new_album = Album(
        1,
        'Title',
        2018,
        1
    )
    new_album1 = Album(
        1,
        'Title',
        2018,
        1
    )

    assert new_album == new_album1