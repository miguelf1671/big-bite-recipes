from app import app
from models import User, Recipe, Favorite, db
from faker import Faker
from random import choice

fake = Faker()


# Create 10 fake recipes
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

# Creates 5 fake users


def create_users():
    users = []
    for _ in range(5):
        users.append(User(
            username=fake.name(),
            user_favorites=fake.word(),
            user_submissions=fake.word(),
        ))
    return users

#########################################################
### Populate table within application context manager ###
#########################################################


with app.app_context():
    print('Populating database...')

    print('\n\t>>> Deleting existing database tables...')
    Recipe.query.delete()
    User.query.delete()
    Favorite.query.delete()
    db.session.commit()
    print('\t>>> Tables deleted.')

    print('\n\t>>> Generating sample data for recipes...')
    recipes = create_recipes()
    db.session.add_all(recipes)
    db.session.commit()
    print('\t>>> Recipe data generation successful.')

    print('\n\t>>> Generating sample data for users...')
    users = create_users()
    db.session.add_all(users)
    db.session.commit()
    print('\t>>> User data generation successful.')

    print('\n>>> Database populated successfully.')
