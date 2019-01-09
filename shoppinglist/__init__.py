from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shopping_list_v1.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from shoppinglist import routes
