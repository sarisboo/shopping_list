from shoppinglist import app
from shoppinglist.models import Recipe, RecipeIngredients, Ingredient, RecipeSchema

recipe_schema = RecipeSchema(many=True, strict=True)
# endpoint to get recipe detail by id
@app.route("/recipes/weekly_suggestions/", methods=["GET"])
def recipe_detail():
    recipes = Recipe.query.order_by("RANDOM()").limit(10).all()
    return recipe_schema.jsonify(recipes)
