from marshmallow import Schema, fields


class Recipe():
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __repr__(self):
        return '< Recipe(name={self.name!r}) > '.format(self=self)

class RecipeSchema(Schema):
    name = fields.String()
    ingredients = fields.List(fields.String())
    instructions = fields.List(fields.String())