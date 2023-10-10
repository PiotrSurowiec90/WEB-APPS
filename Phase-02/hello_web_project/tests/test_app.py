# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""


def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"


# === End Example Code ===


"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""


def test_post_count_vowels_eee(web_client):
    response = web_client.post("/count_vowels", data={"text": "eee"})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == 'There are 3 vowels in "eee"'


"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""


def test_post_count_vowels_eunoia(web_client):
    response = web_client.post("/count_vowels", data={"text": "eunoia"})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == 'There are 5 vowels in "eunoia"'


"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""


def test_post_count_vowels_mercurial(web_client):
    response = web_client.post("/count_vowels", data={"text": "mercurial"})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == 'There are 4 vowels in "mercurial"'


"""
When: I make a POST request to /sort_names
And: I send "Joe,Alice,Zoe,Julia,Kieran" as the body parameter list
Then: I should get a 200 response with sorted list of names.
"""


def test_sort_names_with_form_data(web_client):
    response = web_client.post(
        "/sort_names", data={"list": "Joe,Alice,Zoe,Julia,Kieran"}
    )
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Alice,Joe,Julia,Kieran,Zoe"


def test_names_with_two_names_as_param(web_client):
    response = web_client.get("/names?add=Eddie,Leo")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Alice, Eddie, Julia, Karim, Leo"


def test_names_with_no_params(web_client):
    response = web_client.get("/names")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice, Julia, Karim"


def test_names_with_similar_names(web_client):
    response = web_client.get("/names?add=Aaaa,Aaaz,Aaab")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Aaaa, Aaab, Aaaz, Alice, Julia, Karim"