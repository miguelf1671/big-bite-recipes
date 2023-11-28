from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import User, Recipe, db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///app.db'
migrate = Migrate(app, db)
db.init_app(app)

@app.get('/')
def hope():
    return {'msg': 'I really hope this works!'}

@app.get('/api')
def api():
    return {'msg': 'Getting a little closer to what you are looking for!'}

##########################
### Routes for Recipes ###
##########################

@app.get('/api/recipes')
def get_recipes():
    all_recipes = Recipe.query.all()
    recipe_list = [recipe.to_dict() for recipe in all_recipes]
    return make_response(recipe_list), 200

@app.post('/api/recipes')
def add_recipe():
    POST_REQUEST = request.get_json()
    new_recipe = Recipe(
        name=POST_REQUEST['name'],
        image=POST_REQUEST['image'],
        ingredients=POST_REQUEST['ingredients'],
        directions=POST_REQUEST['directions'],
        vegetarian=POST_REQUEST['vegetarian'],
        who_submitted=POST_REQUEST['who_submitted'],
        who_favorited=POST_REQUEST['who_favorited']
    )
    db.session.add(new_recipe)
    db.session.commit()
    return make_response(jsonify(new_recipe.to_dict())), 201

########################
### Routes for Users ###
########################

@app.get('/api/users')
def get_users():
    all_users = User.query.all()
    user_list = [user.to_dict() for user in all_users]
    return make_response(user_list), 200

if __name__ == '__main__':
    app.run()