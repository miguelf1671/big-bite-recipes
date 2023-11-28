from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Recipe(db.Model, SerializerMixin):
    __tablename__ ='recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    ingredients = db.Column(db.String, nullable=False)
    directions = db.Column(db.String, nullable=False)
    vegetarian = db.Column(db.Boolean, nullable=False)
    who_submitted = db.Column(db.String)
    who_favorited = db.Column(db.String)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    favorites = db.Column(db.String, nullable=False)
    submissions = db.Column(db.String, nullable=False)
