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

    album_divs = page.locator("li")
    expect(album_divs).to_have_text(["Doolittle", "Surfer Rosa"])


"""
GET /albums/<int: album_id>
Test if the requested url returns 200 - OK resposne.
"""


def test_get_album_detail(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.get("/albums/1")
    assert response.status_code == 200


"""
GET /albums/album_id
Test if requested url returns album detail content
"""


def test_get_album_detail_renders_album_indo(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/1")

    album_container = page.locator(".album")
    expect(album_container).to_have_text(["Title: Doolittle Released: 1989"])


"""GET /albums
Test if list of album contains valid links to detail views"""


def test_get_album_list_has_links_to_album_detail(
    page, test_web_address, db_connection
):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")

    page.click("text=Doolittle")

    album_container = page.locator(".album")

    expect(album_container).to_have_text(["Title: Doolittle Released: 1989"])


def test_back_navigation_button_in_album_detail(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")

    page.click("text=Doolittle")
    page.click("text=Go back to list of albums")
    title = page.locator("h1")
    expect(title).to_have_text(["Albums"])


"""GET /artists
Test if artist list view contains list of artists
"""


def test_artist_list_has_list_of_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")

    title = page.locator("h1")
    expect(title).to_have_text(["Artists"])

    artists = page.locator("li")
    expect(artists).to_have_text(["Pixies", "ABBA", "Taylor Swift", "Nina Simone"])


"""GET /artists
Test if artist contain valid link to its detail page"""


def test_artist_list_has_valid_detail_link(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")

    page.click("text=Pixies")
    title = page.locator("h1")
    expect(title).to_have_text(["Pixies"])


"""GET /artist/1
Test if artist detail with artist id = 1 returns template
with correct values"""


def test_artist_detail(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/1")

    title = page.locator("h1")
    expect(title).to_have_text(["Pixies"])

    genre = page.locator("p")
    expect(genre).to_have_text(["Rock"])


"""Get /albums/create
Test page displays form on get request."""


def test_album_create(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add new album")
    page.fill("input[name='title']", "New Album")
    page.fill("input[name='release_year']", "2023")
    page.fill("input[name='artist_id']", "1")
    page.click("text=Create")
    new_album_container = page.locator(".album")
    expect(new_album_container).to_have_text(["Title: New Album Released: 2023"])


def test_album_create_with_invalid_form(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add new album")
    page.click("text=Create")
    errors = page.locator(".errors")
    expect(errors).to_have_text(
        "Title can't be empty!, Release year can't be empty!, Artist id can't be empty!"
    )
