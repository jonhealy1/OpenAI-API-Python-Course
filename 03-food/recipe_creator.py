from recipe import RecipeGenerator
from dalle import Dish2Image

gen = RecipeGenerator()
recipe = gen.generate_recipe()
print(recipe)
dalle = Dish2Image(recipe)
dalle.generate_image()