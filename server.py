from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api
from models.category import Category
from models.dishes import Dish
from db import db
from config import DBUSER,DBHOST,DBPASS
from controllers.categories import CategoriesAll


app = Flask(__name__)
app.config['SECRET_KEY'] = 'kjhgi1723yt172g'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DBUSER}:{DBPASS}@{DBHOST}/postgres'
db.init_app(app)
api = Api(app)
CORS(app)



api.add_resource(CategoriesAll,'/categories')




app.run(debug=True,host='0.0.0.0')