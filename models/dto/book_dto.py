from flask_restplus import Namespace
class BookDTO:
    api = Namespace('user', description='user related operations')
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author