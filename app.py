from flask import Flask, jsonify, request
from database import databuku

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Books API!"

# Function to display all books
@app.route('/api/books', methods=['GET'])
def get_books():
    if not databuku:
        return jsonify({"message": "The books list is empty."}), 404
    return jsonify(databuku), 200

# Function to add a new book
@app.route('/api/books', methods=['POST'])
def add_book():
    new_id = databuku[-1]["id"] + 1 if databuku else 1  # Define new id
    new_book = {
        "id": new_id,
        "title": request.json.get("title"),
        "author": request.json.get("author"),
        "year": request.json.get("year")
    }
    databuku.append(new_book)
    
    return jsonify({"message": "Book successfully added.", "book": new_book}), 201

# Function to display book by id
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in databuku if b["id"] == book_id), None)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

# Function to edit book based on id
@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in databuku if b["id"] == book_id), None)
    if book:
        book["title"] = request.json.get("title", book["title"])
        book["author"] = request.json.get("author", book["author"])
        book["year"] = request.json.get("year", book["year"])
        return jsonify({"message": "Book successfully updated.", "book": book}), 200
    return jsonify({"error": "Book not found"}), 404

# Function to delete book based on id
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((b for b in databuku if b["id"] == book_id), None)
    if book:
        databuku.remove(book)
        return jsonify({"message": "Book successfully deleted."}), 200  # HTTP 200 OK
    return jsonify({"error": "Book not found"}), 404  # HTTP 404 Not Found

if __name__ == '__main__':
    app.run(debug=True)
