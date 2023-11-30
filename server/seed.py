# from app import app
from models import User, Recipe, Favorite
from faker import Faker
from random import choice, randint
from config import db, app
import bcrypt

# seed_value = 123
# fake = Faker()
# Faker.seed(seed_value)


# Create 10 fake recipes
def create_recipes(users):
    

    recipes = []

    recipes.append(Recipe(name="Air Fried Pork Chops", 
                          image="https://www.allrecipes.com/thmb/zNXLTa_UB4K_-QO_NUhTYFd3acQ=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/breaded-air-fryer-pork-chops-photo-by-allrecipes-f7a97cd9ff9a42a39b6bfb7903e125cb.jpg",
                          ingredients="Pork Chops, Croutons, Green Beans, Mashed Potatoes, Eggs",
                          directions="Cook it",
                          vegetarian=False,
                          who_submitted=users[randint(0, len(users)-1)].id,
                          likes=randint(0, len(users)-1)
                          ))
    recipes.append(Recipe(name="Dijon Salmon",
                          image="https://www.allrecipes.com/thmb/-aP8PF7KwqeY9mCGyUievMtxnpI=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/baked-salmon-fillets-dijon-photo-by-allrecipes-6b03f1ff03874d4894de4faa51ccf27a.jpg",
                          ingredients="Salmon, Asparagus, Breadcrumbs, Rice Pilaf, Dijon Mustard",
                          directions="Cook it",
                          vegetarian=False,
                          who_submitted=users[randint(0, len(users)-1)].id,
                          likes=randint(0, len(users)-1)
                          ))
    recipes.append(Recipe(name="Sliced Ribeye",
                          image="https://www.allrecipes.com/thmb/4B-y1Djh6CEhQvy8iVThVUXjE5g=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/sliced-ribeye-and-arugula-on-texas-toast-photo-by-allrecipes-2e78db0f7dd24ace80774f48d458ab3b.jpg",
                          ingredients="Steak, Carrots, Arugula, Lemon, Texas Toast",
                          directions="Cook It",
                          vegetarian=False,
                          who_submitted=users[randint(0, len(users)-1)].id,
                          likes=randint(0, len(users)-1)
                          ))
    recipes.append(Recipe(name="Spaghetti Squash",
                          image="https://www.allrecipes.com/thmb/SUzV-r_5VTZ2XvYNrv5XKN8lYzQ=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/baked-spaghetti-squash-with-beef-and-veggies-photo-by-allrecipes-c88be3977847456ead61e7cbb0b9e54b.jpg",
                          ingredients="Spaghetti Squash, Cheddar Cheese, Tomatoes, Ground Beef, Frozen Pepper Stir-Fry Mix",
                          directions="Cook It",
                          vegetarian=False,
                          who_submitted=users[randint(0, len(users)-1)].id,
                          likes=randint(0, len(users)-1)
                          ))
    recipes.append(Recipe(name="Easy Enchiladas",
                          image="https://www.allrecipes.com/thmb/tjeU3pk0tHF1hTEBkV8T8FaU3Ng=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/easy-enchiladas-photo-by-allrecipes-04579001f9d94221aa5ff753d0729e34.jpg",
                          ingredients="Ground Beef, Salsa con Queso, Salsa, Tortillas, Cheddar-Monterey Jack Cheese",
                          directions="Cook It",
                          vegetarian=False,
                          who_submitted=users[randint(0, len(users)-1)].id,
                          likes=randint(0, len(users)-1)
                          ))
    recipes.append(Recipe(name="Tomato Feta Pasta",
                          image="https://www.allrecipes.com/thmb/AoUAjMbyeZhbF9ejq7lPdO_owd4=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/tomato-feta-pasta-photo-by-allrecipes-c2b6249b301d4998a1b2a4e0720cd8b0.jpg",
                          ingredients="Cherry Tomatoes, Feta Cheese, Basil, Garlic, Pasta",
                          directions="Cook It!",
                          vegetarian=False,
                          who_submitted=users[randint(0, len(users)-1)].id,
                          likes=randint(0, len(users)-1)
                          ))
    recipes.append(Recipe(name="Buffalo Chicken Lettuce Wraps",
                          image="https://www.allrecipes.com/thmb/bSjpK4ykC_rRGLi7IzKeWWdXHfU=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/slow-cooker-buffalo-chicken-lettuce-wraps-photo-by-allrecipes-2fd18ae5282844838e7ada69e1137ad3.jpg",
                          ingredients="Chicken Breasts, Ranch Seasoning, Buffalo Hot Sauce, Lettuce, Blue Cheese",
                          directions="Cook It",
                          vegetarian=False,
                          who_submitted=users[randint(0, len(users)-1)].id,
                          likes=randint(0, len(users)-1)
                          ))
    recipes.append(Recipe(name="BBQ Chicken Pizza",
                          image="https://www.allrecipes.com/thmb/sm9fmePDpge8Cq3EC6UPp-NNzTw=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/bbq-chicken-pizza-photo-by-allrecipes-18f854728c924957b13ef0b7e33c3efd.jpg",
                          ingredients="Pizza Dough, Rotisserie Chicken, Mozzerella Cheese, BBQ Sauce, Red Onion",
                          directions="Cook It",
                          vegetarian=False,
                          who_submitted=users[randint(0, len(users)-1)].id,
                          likes=randint(0, len(users)-1)
                          ))
    recipes.append(Recipe(name="Chorizo Street Tacos",
                          image="https://www.allrecipes.com/thmb/0V102fvzkOy9ksHH2NX1vMFRb5U=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/easy-chorizo-street-tacos-photo-by-allrecipes-640b12a6c2d94e0593fda0e900551b79.jpg",
                          ingredients="Chorizo, Corn Tortillas, Onion, Cilantro",
                          directions="Cook It",
                          vegetarian=False,
                          who_submitted=users[randint(0, len(users)-1)].id,
                          likes=randint(0, len(users)-1)
                          ))
    recipes.append(Recipe(name="Thai Coconut Pork Curry",
                          image="https://www.allrecipes.com/thmb/8aON0PqCDKxpOMqQfsGbFiKD_HU=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/thai-coconut-pork-curry-photo-by-allrecipes-e0f5aaf35e5f4e9d9f1fcd51e43bcc08.jpg",
                          ingredients="Pork, Thai Coconut Curry Stir-Fry Sauce, Rice, Bell Pepper, Sugar Snap Peas",
                          directions="Cook It",
                          vegetarian=False,
                          who_submitted=users[randint(0, len(users)-1)].id,
                          likes=randint(0, len(users)-1)
                          ))
    
    return recipes

# Creates 5 fake users

def create_users():
    def encrypt_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt=salt)
        return hashed_password.decode("utf-8")
    users = []
    users.append(User(username="Tymur Bondar", password=encrypt_password("tm123")))
    users.append(User(username="Andrew Blumenthal", password=encrypt_password("ab123")))
    users.append(User(username="Jason Phillips", password=encrypt_password("jp123")))
    users.append(User(username="Dennis Shin", password=encrypt_password("ds123")))
    users.append(User(username="Sophie Gamer", password=encrypt_password("sg123")))
    users.append(User(username="Miguel Flores", password=encrypt_password("mf123"), is_admin=True))
    users.append(User(username="Morgan Deason", password=encrypt_password("md123"), is_admin=True))
    
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
