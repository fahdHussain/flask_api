from flask import Flask, jsonify, request
import json
from main.model.recipe import Recipe, RecipeSchema

app = Flask(__name__)

with open("./data/data.json") as d:
    data = json.load(d)

@app.route("/recipes", methods=['GET','POST','PUT'])
def recipes():
    schema = RecipeSchema(many=True,)
    recipes = schema.dump(data['recipes'])
    recipeNames = {'recipeNames':[]}
    for i in recipes:
        recipeNames['recipeNames'].append(i['name'])

    if request.method == 'GET':
        return jsonify(recipeNames),200
    if request.method == 'POST':
        post_data = request.get_json()
        new_recipe = post_data['name']
        if new_recipe in recipeNames['recipeNames']:
            return jsonify({"error": "recipe  already exists"}),400
        else:
            data['recipes'].append(request.get_json())
            return '',201
    if request.method == 'PUT':
        put_data = request.get_json()
        put_name = put_data['name']
        if put_name not in recipeNames['recipeNames']:
            return jsonify({"error": "recipe  does not exist"}),400
        else:
            for val,i in enumerate(data['recipes']):
                if i['name'] == put_name:
                    data['recipes'][val] = put_data
                    return "", 204
@app.route("/recipes/details/<name>", methods=['GET','POST'])
def ingredients(name):
    if request.method == 'GET':
        schema = RecipeSchema(many=True)
        recipes = schema.dump(data['recipes'])
        iandst = {'ingredients':[],'numSteps:':0}
        exists_flag = False
        for i in recipes:
            if i['name'] == name:
                iandst['ingredients'] = i['ingredients']
                iandst['numSteps:'] = len(i['instructions'])
                exists_flag = True
        if(exists_flag):
            details = {'details':{'ingredients':iandst['ingredients'], 'numSteps': iandst['numSteps:']}}
        else:
            details = {}
        return jsonify(details), 200
