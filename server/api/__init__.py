from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from os import path

ma = Marshmallow()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.app_context().push()

    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(ma)

    from .models import Product
    from .views import views

    create_database()

    app.register_blueprint(views, url_prefix="/")

    return app


def create_database():
    if not path.exists(Config.SQLALCHEMY_DATABASE_URI):
        db.create_all()
        print("DB created!")
