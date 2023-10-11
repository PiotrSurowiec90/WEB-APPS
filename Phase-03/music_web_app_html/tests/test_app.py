from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""


def test_get_emoji(page, test_web_address):  # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")


# === End Example Code ===

"""
GET /albums
Test if page contains albums reflecting databasae"""


def test_get_albums_returns_200_OK(web_client):
    response = web_client.get("/albums")
    assert response.status_code == 200


def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")

    album_divs = page.locator(".album")
    expect(album_divs).to_have_text(
        ["Title: Doolittle Released: 1989", "Title: Surfer Rosa Released: 1988"]
    )
