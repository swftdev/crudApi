from flask import Flask, jsonify, request
from models.db import init_app, get_db
from models import Book

app = Flask(__name__)
init_app(app)

@app.route("/", methods=["GET", "POST"])
def books():
    db = get_db()
    if request.method == "GET":
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

    if request.method == "POST":
        book = request.json
        newBook = Book(
            title=book["title"],
            author=book["author"]
        )
        db.add(newBook)
        db.commit()
        return jsonify(newBook.as_dict())


@app.route("/<id>", methods=["GET", "PUT", "DELETE"])
def book_by_id(id):
    db = get_db()
    # GET book by id
    if request.method == "GET":
        book = db.query(Book).get(id)
        if book:
            return jsonify({
                "id": book.id,
                "author": book.author,
                "title": book.title
            })
        return jsonify({})

    elif request.method == "PUT":
        data = request.json
        newBook = {
            "author": data["author"],
            "title": data["title"]
        }
        db.query(Book).filter_by(id=id).update(newBook)
        db.commit()
        return jsonify(newBook)
    
    elif request.method == "DELETE":
        db.query(Book).filter_by(id=id).delete()
        db.commit()
        return "OK", 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)