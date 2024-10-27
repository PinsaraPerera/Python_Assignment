import os
import json

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

class RecipeBook:
    def __init__(self):
        self.recipes_dict = {}

    def add_recipe(self, recipe):
        """
        First check if the file 'recipes.json' exists.
        If it does, open it and load the content to the variable self.recipes_dict. Then, update the dictionary with the new recipe.
        Finally, write the updated dictionary to the file 'recipes.json'. If the file does not exist, create it and write the recipe to it.
        The format of the dictionary should be as follows:
        {
            'recipe_name': {
                'ingredients': ['ingredient_1', 'ingredient_2', ...],
                'instructions': ['instruction_1', 'instruction_2', ...]
            }
        }
        """

        _recipe = {recipe.name: {'ingredients': recipe.ingredients, 'instructions': recipe.instructions}}
        
        try:
            if os.listdir('recipes.json'):
                with open('recipes.json', 'r') as f:
                    self.recipes_dict = json.load(f)
        except:
            pass

        self.recipes_dict.update(_recipe)

        with open('recipes.json', 'w') as f:
            json.dump(self.recipes_dict, f)

            

    def search_recipe(self, name):
        """
        In this function, search for a recipe by name. If the recipe is found, return the recipe object. If not, return None.
        """
        for recipe in self.recipes_dict:
            if recipe == name:
                return Recipe(recipe, self.recipes_dict[recipe]['ingredients'], self.recipes_dict[recipe]['instructions'])
            
        return None

    def remove_recipe(self, name):
        del self.recipes_dict[name]

    def print_recipes(self):
        for recipe in self.recipes_dict:
            print(recipe)
            print("Ingredients: ", self.recipes_dict[recipe]['ingredients'])
            print("Instructions: ", self.recipes_dict[recipe]['instructions'])
            print("\n")

# create some recipes
recipe1 = Recipe("Tea", ["Tea bag", "Water"], ["Boil water", "Steep tea bag in water", "Add sugar if desired"])
recipe2 = Recipe("Omlette", ["Eggs", "Salt", "Pepper", "Cheese", "Tomato", "Onion"], ["Beat eggs", "Chop vegetables", "Add vegetables to eggs", "Cook on low heat"])
recipe3 = Recipe("Dhal Curry", ["Lentils", "Water", "Turmeric", "Salt", "Pepper", "Chili powder", "Curry leaves"], ["Boil lentils", "Add spices", "Cook until thick"])

# create a recipe book
book = RecipeBook()

# add the recipes to the recipe book
book.add_recipe(recipe1)
book.add_recipe(recipe2)
book.add_recipe(recipe3)

# search for a recipe
recipe = book.search_recipe("Omlette")
print("Recipe found: ", recipe.name)
print("Ingredients: ", recipe.ingredients)
print("Instructions: ", recipe.instructions)

# remove a recipe
book.remove_recipe("Omlette")
print("\nRecipe removed\n")

# print all recipes
book.print_recipes()

