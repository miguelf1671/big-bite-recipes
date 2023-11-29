from app import app
from models import User, Recipe, Favorite, db
from faker import Faker
from random import choice, randint

seed_value = 123
fake = Faker()
Faker.seed(seed_value)


# Create 10 fake recipes
def create_recipes(users):

    recipes = []

    for _ in range(10):
        recipes.append(Recipe(
            name=fake.name(),
            image=fake.image_url(),
            ingredients=fake.paragraph(),
            directions=fake.paragraph(),
            vegetarian=choice([True, False]),
            who_submitted=users[randint(0, len(users)-1)].username,
            likes=randint(0, len(users)-1)
        ))

    


    return recipes

# Creates 5 fake users

def create_users():
    users = []
    for _ in range(5):
        users.append(User(
            username=fake.name()
        ))
    return users


def create_favorites(recipes, users):
    list_of_favorites = []

    for _ in range(len(recipes)):

        list_of_favorites.append(Favorite(
            recipe_id=recipes[randint(0, len(recipes) - 1)].id,
            user_id=users[randint(0, len(users) - 1)].id
        ))

    return list_of_favorites


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

    print('\n\t>>> Generating sample data for users...')
    users = create_users()
    db.session.add_all(users)
    db.session.commit()
    print('\t>>> User data generation successful.')

    print('\n\t>>> Generating sample data for recipes...')
    recipes = create_recipes(users)
    db.session.add_all(recipes)
    db.session.commit()
    print('\t>>> Recipe data generation successful.')

    print('\n\t>>> Generating sample data for favorites...')
    favorites = create_favorites(recipes, users)
    db.session.add_all(favorites)
    db.session.commit()
    print('\t>>> Favorite data generation successful.')

    print('\n>>> Database populated successfully.')
