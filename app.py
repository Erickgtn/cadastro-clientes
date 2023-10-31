from flask import Flask
from setting import Config
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api



db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

    db.init_app(app)
    api = Api(app)
    init_routes(api)

    return app

def init_routes(api):
    from controllers.book_controller import BookController

    api.add_resource(BookController,  '/books', '/books/<int:book_id>')
