# Tests for your routes go here
from lib.album import Album

"""
POST /albums
Create new album
"""


def test_post_albums_with_new_album(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    response = web_client.post(
        "/albums", data={"title": "new_album", "release_year": 2023, "artist_id": 1}
    )
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Album created!"
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert (
        response.data.decode("utf-8") == f"{str(Album(1, 'title1', 2023, 1))}\n"
        f"{str(Album(2, 'title2', 2023, 2))}\n{str(Album(3, 'title3', 2023, 3))}\n"
        f"{str(Album(4, 'new_album', 2023, 1))}"
    )


def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    resposnse = web_client.get("/artists")
    assert resposnse.status_code == 200
    assert resposnse.data.decode("utf-8") == "artist1, artist2, artist3"


"""POST /artists
expected resposne status code -200
expected: new artist included in artist list"""

def test_post_artist_with_valid_form_data(web_client, db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    resposnse = web_client.post("/artists", data = {
        'name': 'artist4',
        'genre': 'genre4'
    })
    assert resposnse.status_code == 200

    resposnse = web_client.get("/artists")
    assert resposnse.status_code == 200
    assert resposnse.data.decode("utf-8") == "artist1, artist2, artist3, artist4"

def test_post_artists_with_invalid_form_data(web_client,db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    resposnse = web_client.post("/artists")
    assert resposnse.status_code == 400
    assert resposnse.data.decode("utf-8") == "Form data is invalid!"
