from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    total_time = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Recipe ('{self.name}', '{self.rating}','{self.total_time}' )"


class Ingredient(db.Model):
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"Recipe ('{self.name}')"


class RecipeIngredients(db.Model):
    __tablename__ = "recipes_ingredients"

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"))
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"))
    quantity = db.Column(db.Integer)


class RecipeSchema(ma.Schema):
    class Meta:
        fields = ("name", "rating", "total_time")


recipe_schema = RecipeSchema(many=True, strict=True)

# endpoint to get recipe detail by id
@app.route("/recipes/weekly_suggesions", methods=["GET"])
def recipe_detail():
    recipes = Recipe.query.order_by("RANDOM()").limit(10).all()
    return recipe_schema.jsonify(recipes)


def run():
    app.run()


if __name__ == "__main__":
    run()
