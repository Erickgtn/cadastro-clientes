from flask import request
from flask_restful import Resource
from services.book_service import BookService


class BookController(Resource):
    def __init__(self):
        self.book_service = BookService()

    def get(self, book_id=None):
        if book_id:
            book = self.book_service.get_book_by_id(book_id)
            if book:
                return book, 200
            else:
                return {"message": "Book not found"}, 404
        else:
            books = self.book_service.get_all_books()
            return books, 200

    def post(self):
        book_data = request.json
        new_book = self.book_service.add_book(book_data)
        return new_book, 201

    def put(self, book_id):
        book_data = request.json
        updated_book = self.book_service.update_book(book_id, book_data)
        if updated_book:
            return updated_book, 200
        else:
            return {"message": "Book not found"}, 404

    def delete(self, book_id):
        success = self.book_service.delete_book(book_id)
        if success:
            return {"message": "Book deleted successfully"}, 200
        else:
            return {"message": "Book not found"}, 404
