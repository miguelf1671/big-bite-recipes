from app import app
from models import User, Recipe, db
from faker import Faker
from random import choice

fake = Faker()

def create_recipes():
    recipes = []
    for _ in range(10):
        recipes.append(Recipe(
            name=fake.name(),
            image=fake.image_url(),
            ingredients=fake.paragraph(),
            directions=fake.paragraph(),
            vegetarian=choice([True, False]),
            who_submitted=fake.name(),
            who_favorited=fake.name()
        ))
    return recipes


def create_users():
    users = []
    for _ in range(5):
        users.append(User(
            username=fake.name(),
            favorites="Hopefully a future list",
            submissions="Hopefully a future list",
        ))
    return users


with app.app_context():
    Recipe.query.delete()
    User.query.delete()
    db.session.commit()

    recipes = create_recipes()
    db.session.add_all(recipes)
    db.session.commit()

    users = create_users()
    db.session.add_all(users)
    db.session.commit()
