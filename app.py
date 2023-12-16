from flask import Flask, jsonify, request
from models.db import init_app, get_db
from models import Book

app = Flask(__name__)
init_app(app)

@app.route("/")
def get_book():
    db = get_db()
    results = []
    books = db.query(Book).all()
    for b in books:
        book = {
            "id": b.id,
            "author": b.author,
            "title": b.title
        }
        results.append(book)

    return jsonify(results)

@app.route("/init", methods=["GET"])
def init_book():
    # look at how we use the request payload / body
    # get the title and the author from there
    # change this from a get -> post
    # use postman to post a new book, then use / route to see the book
    db = get_db()
    newBook = Book(title="demo", author="something")
    db.add(newBook)
    db.commit()
    return "Hello", 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)