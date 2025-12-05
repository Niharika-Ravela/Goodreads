# Goodreads Surprise Book Picker 📚🎡  

A Python-based project that fetches books from a Goodreads shelf using RSS scraping and displays a randomly selected book through a simple UI.

This app solves a fun real-world problem:  
> **“I have too many unread books. Which one should I read next?”**

It uses Python for data extraction and a lightweight frontend for visualization.

---

## ⭐ Features

### 🔍 Goodreads Scraper (`scraper.py`)
- Fetches your Goodreads shelf via **RSS feed**
- Parses book titles, authors, and links
- Cleans and structures data into a usable format

### 🌐 Web App (`app.py` + `static/index.html`)
- Python backend (Flask or similar framework)
- Serves a simple interactive UI from `static/index.html`
- Displays:
  - Randomly selected book
  - Title
  - Author
  - Goodreads link or cover (if available)
- Uses `placeholder.png` as part of the UI (wheel, background, or icon)

---

## 🧰 Tech Stack

- **Python 3.8+**
- **Flask** (or whichever framework you used)
- **Requests / feedparser** (or similar RSS parsing libraries)
- **HTML, CSS, JavaScript** (in `static/index.html`)

Check `requirements.txt` for the full dependency list.

---
## 🎥 Demo

You can watch a short demo of the Goodreads Surprise Book Picker here:
[▶ Watch the demo](assets/result.mp4)

## 📁 Project Structure

```plaintext
Goodreads/
├── app.py                # Backend server
├── scraper.py            # Goodreads RSS scraper logic
├── requirements.txt      # Python dependencies
├── static/               # Frontend files
│   ├── index.html        # Main UI
│   └── placeholder.png   # UI asset
└── README.md
