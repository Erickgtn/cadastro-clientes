from app import db
from models.entity.book import Book

# Example data
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]

class BookService:
    def get_all_books(self):
        return books

    def get_book_by_id(self, book_id):
        return next((b for b in books if b['id'] == book_id), None)

    def add_book(self, book_data):
        new_book = {
            "id": book_data['id'],
            "title": book_data['title'],
            "author": book_data['author']
        }
        book = Book(new_book["id"], new_book["title"], new_book["author"])
        db.session.add(book)
        db.session.commit()
        return new_book

    def update_book(self, book_id, book_data):
        book = next((b for b in books if b['id'] == book_id), None)
        if book:
            book['title'] = book_data['title']
            book['author'] = book_data['author']
            return book
        else:
            return None

    def delete_book(self, book_id):
        book = next((b for b in books if b['id'] == book_id), None)
        if book:
            books.remove(book)
            return True
        else:
            return False