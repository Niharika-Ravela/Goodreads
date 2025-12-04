# Goodreads Surprise Book Picker 📚✨  
A fun, interactive book-randomizer app that pulls books directly from my **Goodreads shelf** using the RSS feed and displays a randomly selected book using a spinning-wheel UI.

This project solves a real personal problem:  
> *“I own many unread books. Which one should I read next?”*

---

## 🎯 Features

- Fetches books from a **Goodreads shelf via RSS**  
- Cleans + parses book data using JavaScript  
- Displays books on a **spinner wheel UI**  
- Randomly selects a book when you click “Spin”  
- Highlights the final chosen book with:
  - Title  
  - Author  
  - Cover (if available)  

---

## 🧠 How It Works

1. The RSS feed from Goodreads is fetched directly using JavaScript  
2. The XML is parsed and converted into a book list  
3. A wheel UI is dynamically generated  
4. CSS animations create the spinning effect  
5. A random book is selected when the wheel stops

---

## 🛠 Tech Stack

- **HTML5**  
- **CSS3**  
- **Vanilla JavaScript**  
- RSS Feed Parsing  
- DOM Manipulation  
- Spinner Animation Logic  

This project intentionally avoids frameworks to keep it lightweight and easy to understand.

---

## 📂 Folder Structure

```plaintext
Goodreads/
├── index.html
├── styles.css
├── script.js
├── images/  
└── README.md
