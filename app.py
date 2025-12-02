# app.py
import os
import requests
from flask import Flask, jsonify, request, send_from_directory
from dotenv import load_dotenv
from scraper import fetch_books_from_rss

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY", "").strip()
# fallback placeholder image path (you uploaded this image earlier)
PLACEHOLDER_IMAGE_PATH = "C:\\Users\\nihar\\OneDrive\\Desktop\\Projects\\Goodreads Project\\goodreads-wheel\\static\\placeholder.png"

app = Flask(__name__, static_folder="static", static_url_path="/static")

def google_books_cover(title, author=""):
    """
    Query Google Books server-side for best cover image.
    Returns cover URL or None.
    """
    if not title:
        return None

    # Build best-effort query
    q = f'intitle:{title}'
    if author:
        q += f'+inauthor:{author}'

    params = {"q": q, "maxResults": 5}
    if GOOGLE_API_KEY:
        params["key"] = GOOGLE_API_KEY

    try:
        resp = requests.get("https://www.googleapis.com/books/v1/volumes", params=params, timeout=8)
        if resp.status_code != 200:
            return None
        data = resp.json()
        if data.get("items"):
            for item in data["items"]:
                info = item.get("volumeInfo", {})
                imgs = info.get("imageLinks", {})
                # choose best available
                candidate = imgs.get("extraLarge") or imgs.get("large") or imgs.get("medium") or imgs.get("thumbnail") or imgs.get("smallThumbnail")
                if candidate:
                    # ensure https
                    if candidate.startswith("http://"):
                        candidate = candidate.replace("http://", "https://", 1)
                    return candidate
        # fallback: try looser search by title only
        params2 = {"q": f'intitle:{title}', "maxResults": 3}
        if GOOGLE_API_KEY:
            params2["key"] = GOOGLE_API_KEY
        resp2 = requests.get("https://www.googleapis.com/books/v1/volumes", params=params2, timeout=6)
        if resp2.status_code == 200:
            data2 = resp2.json()
            if data2.get("items"):
                for item in data2["items"]:
                    info = item.get("volumeInfo", {})
                    imgs = info.get("imageLinks", {})
                    candidate = imgs.get("thumbnail") or imgs.get("smallThumbnail")
                    if candidate:
                        if candidate.startswith("http://"):
                            candidate = candidate.replace("http://", "https://", 1)
                        return candidate
    except Exception:
        pass

    return None

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/api/books")
def api_books():
    """
    Return the live list of books from Goodreads RSS.
    """
    try:
        books = fetch_books_from_rss()
        return jsonify({"count": len(books), "books": books})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/cover")
def api_cover():
    """
    Given title & author (query params), return a cover URL.
    If none found, returns the placeholder path.
    """
    title = request.args.get("title", "")
    author = request.args.get("author", "")
    if not title:
        return jsonify({"error": "Missing title"}), 400

    cover = google_books_cover(title, author)
    if not cover:
        # return the uploaded placeholder path as fallback (see note below)
        cover = PLACEHOLDER_IMAGE_PATH

    return jsonify({"title": title, "author": author, "cover": cover})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
