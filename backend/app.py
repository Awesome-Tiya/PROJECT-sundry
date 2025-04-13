from flask import (
    Flask,
    send_from_directory,
    render_template,
    request,
    jsonify,
)
from flask_cors import CORS, cross_origin
import numpy as np
from fuzzywuzzy import fuzz
from bs4 import BeautifulSoup
import requests
import cv2
import matplotlib
import matplotlib.pyplot as plt
import skimage
import qrcode
import os

matplotlib.use("Agg")
app = Flask(__name__)
CORS(
    app,
    supports_credentials=True,
    resources={
        r"/*": {
            "origins": [
                "http://localhost:5173",
                "http://127.0.0.1:5173",
                "https://crispy-couscous-5p5wrgj9x7j2v4x9-5173.app.github.dev",
            ]
        }
    },
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/genqr", methods=["POST", "OPTIONS"])
@cross_origin(
    origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://crispy-couscous-5p5wrgj9x7j2v4x9-5173.app.github.dev",
    ],
    supports_credentials=True,
    allow_headers=["Content-Type"],
    methods=["POST", "OPTIONS"],
)
def genqr():
    if request.method == "OPTIONS":
        print("Preflight OPTIONS received")
        return jsonify({"message": "Preflight accepted"}), 200

    print("Origin:", request.headers.get("Origin"))
    print("Method:", request.method)
    site = request.json.get("site", "")
    if not site:
        return jsonify({"error": "No data provided"}), 400
    color1 = request.json.get("color1", "")
    color2 = request.json.get("color2", "")
    if color1 != "black" and color2 != "white":
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(site)
        qr.make(fit=True)
        siteqr = qr.make_image(fill_color=color1, back_color=color2)
    else:
        siteqr = qrcode.make(site)
    # siteqr.save("static/siteqr.png")
    static_path = os.path.join(app.root_path, "static", "siteqr.png")
    siteqr.save(static_path)
    return jsonify(
        {"message": "QR Code saved as 'siteqr.png'", "image_url": "/static/siteqr.png"}
    )


@app.route("/books", methods=["POST"])
def books():
    genre = request.json.get("genre", "")
    if genre == "":
        genre = "Art"
    genre = genre.lower()
    try:
        url = "https://www.goodreads.com/shelf/show/" + genre
    except ValueError:
        url = (
            "https://www.goodreads.com/blog/show/2687"
            "-goodreads-members-76-most-popular-books-of-"
            "the-past-decade?ref=decadepopular2023_eb"
        )
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            "AppleWebKit/537.36 (KHTML, like Gecko)"
            "Chrome/91.0.4472.124 Safari/537.36"
        )
    }
    req = requests.get(url, headers=headers)
    req2 = req.text
    soup = BeautifulSoup(req2, "lxml")
    a = soup.find_all("a", class_="bookTitle")
    books = [i.get_text() for i in a]
    if len(books) < 1:
        return jsonify(
            {"genre": "This genre is not valid. Enter correct genre.", "books": books}
        )
    return jsonify({"genre": "", "books": books})


@app.route("/compare", methods=["POST"])
def compare():
    text_1 = request.json.get("text_1", "")
    text_2 = request.json.get("text_2", "")
    ratio = fuzz.ratio(text_1, text_2)
    partial_ratio = fuzz.partial_ratio(text_1, text_2)
    token_sort_ratio = fuzz.token_sort_ratio(text_1, text_2)
    return jsonify(
        {
            "similarity_percentage": ratio,
            "similarity_partial_percentage": partial_ratio,
            "similarity_without_minor_components": token_sort_ratio,
        }
    )


@app.route("/color-effect", methods=["POST"])
@cross_origin(origins="http://localhost:5173")
def color_effect():
    col = request.form.get("col", "")
    name = request.form.get("name", "")
    img1 = request.files.get("img1", "")
    name1 = f"static/{name}.jpg"

    try:
        img = skimage.io.imread(img1)
    except Exception as e:
        return jsonify({"error": f"Could not read the image. {str(e)}"}), 400

    def purple(img):
        # Convert RGBA to RGB
        if img.shape[2] == 4:
            img = img[:, :, :3]
        purple_filter = np.array([[0.5, 0.7, 0.2], [0.7, 0.1, 0.3], [0.7, 0.3, 0.4]])
        purple_img = img.dot(purple_filter.T)
        purple_img /= purple_img.max()
        return purple_img

    purple_demo = purple(img)

    def green(img):
        if img.shape[2] == 4:  # Convert RGBA to RGB
            img = img[:, :, :3]
        green_filter = np.array([[0.1, 0.9, 0.4], [0.77, 0.2, 0.9], [0.1, 0.93, 0.45]])
        green_img = img.dot(green_filter.T)
        green_img /= green_img.max()
        return green_img

    green_demo = green(img)

    def grey(img):
        if img.shape[2] == 4:  # Convert RGBA to RGB
            img = img[:, :, :3]
        grey_filter = np.array([[0.9, 0.9, 0.9], [0.9, 0.9, 0.9], [0.9, 0.9, 0.9]])
        grey_img = img.dot(grey_filter.T)
        grey_img /= grey_img.max()
        return grey_img

    grey_demo = grey(img)

    def blue(img):
        if img.shape[2] == 4:  # Convert RGBA to RGB
            img = img[:, :, :3]
        blue_filter = np.array([[0.9, 0.1, 2.0], [2.0, 0.1, 0.1], [0.1, 0.1, 0.1]])
        blue_img = img.dot(blue_filter.T)
        blue_img /= blue_img.max()
        return blue_img

    blue_demo = blue(img)

    if "1" == col or "green" == col.lower():
        plt.subplot(1, 1, 1)
        window_name = "image"
        cv2.imshow(window_name, green_demo)
        # this line is commented
        # because it does not open
        # a window at vs code codespace.
        # It can be uncommented in
        # an environment where a window can
        # be opened to preview the image file
        cv2.imwrite(name1, 255 * green_demo)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        return jsonify({"image_url": f"/{name1}"})
    elif "2" == col or "blue" == col.lower():
        plt.subplot(1, 1, 1)
        window_name = "image"
        cv2.imshow(window_name, blue_demo)
        # this line is commented
        # because it does not open
        # a window at vs code codespace.
        # It can be uncommented in
        # an environment where a window can
        # be opened to preview the image file
        cv2.imwrite(name1, 255 * blue_demo)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        return jsonify({"image_url": f"/{name1}"})
    elif "3" == col or col.lower() in ["grey", "gray"]:
        plt.subplot(1, 1, 1)
        window_name = "image"
        cv2.imshow(window_name, grey_demo)
        # this line is
        # commented because it
        # does not open a window at vs code codespace.
        # It can be uncommented in an
        # environment where
        # a window can be opened to preview the image file
        cv2.imwrite(name1, 255 * grey_demo)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        return jsonify({"image_url": f"/{name1}"})
    elif "4" == col or "purple" == col.lower():
        plt.subplot(1, 1, 1)
        window_name = "image"
        cv2.imshow(window_name, purple_demo)
        # this line is commented
        # because it does
        # not open a window at vs code codespace.
        # It can be uncommented in
        # an environment where
        # a window can be opened
        # to preview the image file
        cv2.imwrite(name1, 255 * purple_demo)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        return jsonify({"image_url": f"/{name1}"})
    else:
        return jsonify("not a valid color effect name or number")


@app.route("/static/<imgname>")
def serve_static(imgname):
    return send_from_directory("static", imgname)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
