# Tests for your routes go here
from lib.album import Album
"""
POST /albums
Create new album
"""

def test_post_albums_with_new_album(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    response = web_client.post("/albums", data = {
        "title": 'new_album',
        "release_year": 2023,
        "artist_id": 1
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album created!"
    response  = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == str(Album(1, 'new_album', 2023, 1))
