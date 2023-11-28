from flask import Flask
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

if __name__ == '__main__':
    app.run()