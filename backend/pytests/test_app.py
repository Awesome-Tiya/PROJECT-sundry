import sys
import pytest
import requests_mock
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# def test_color_effect(client):
#     col = "1"
#     name = "a"
#     img1 = os.path.join(os.path.dirname(__file__), "../static/FEKEub7aMAIAzE0.jpg")
#     with open(img1, "rb") as img_file:
#         data = {"col": col, "name": name, "img1": (img_file, img1)}
#         response = client.post(
#             "/color-effect", data=data, content_type="multipart/form-data"
#         )
#     assert response.status_code == 200
#     assert response.json["image_url"] == f"/static/{name}.jpg"


def test_compare(client):
    text_1 = "abcde"
    text_2 = "abcdefghij"
    response = client.post("/compare", json={"text_1": text_1, "text_2": text_2})
    assert response.status_code == 200
    assert response.json["similarity_percentage"] == 67

    assert response.json["similarity_partial_percentage"] == 100
    assert response.json["similarity_without_minor_components"] == 67


def test_genqr(client):
    site = "abcde"
    color1 = "green"
    color2 = "yellow"
    response = client.post(
        "/genqr", json={"site": site, "color1": color1, "color2": color2}
    )
    # Assert the status code and response content
    assert response.status_code == 200
    assert response.json["message"] == "QR Code saved as 'siteqr.png'"
    assert response.json["image_url"] == "/static/siteqr.png"

    # Check if the file has been saved in the correct location
    file_path = os.path.join(os.path.dirname(__file__), "../static/siteqr.png")
    assert os.path.exists(file_path), "QR code image was not saved."


def test_books(client):
    genre = "romance"
    mocked_html = """
    <html><body>
        <a class="bookTitle">Book One</a>
        <a class="bookTitle">Book Two</a>
    </body></html>
    """
    with requests_mock.Mocker() as mock:

        mock.get(f"https://www.goodreads.com/shelf/show/{genre}", text=mocked_html)
        response = client.post("/books", json={"genre": genre})
        assert response.status_code == 200
        assert "books" in response.json
        assert response.json["books"] == ["Book One", "Book Two"]
