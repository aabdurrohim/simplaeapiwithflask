# Simple API Demo using Flask

Restfull API using Python with Flask as a framework

## Instalation

run this command on terminal to install Flask

```bash
pip install flask
```
and run the project with command

```bash
python app.py
```

The server will start running at http://127.0.0.1:5000/.

## Endpoints

1. GET /books - Retrieve a list of all books.
   ```bash
   http://127.0.0.1:5000/books
   ```
2. GET /books/id - Retrieve a specific book by ID.
   ```bash
   http://127.0.0.1:5000/books/<id>
   ```
3. POST /books - Create a new book.
   ```
   bash http://127.0.0.1:5000/books
   ```
Under the Body tab, select raw and choose JSON from the dropdown.
Enter the user data as JSON, for example:

```bash
{
    "title": "Negeri Para Bedebah",
    "author": "Tere Liye",
    "year": 2021
}
```
4. PUT /books/<id> - Update an existing book by ID.
5. DELETE /books/<id> - Delete a book by ID.
