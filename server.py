from flask import Flask, render_template, redirect, request
from pymongo import MongoClient
from flask_restful import Api, Resource


import sqlite3

app = Flask(__name__)
api = Api(app)

# Créez une connexion à la base de données SQLite
client = MongoClient('mongodb://localhost:27017/')
db = client['mp']
ingredients_collection = db['ingredients']
events_collection = db['events']

url = "mongodb://localhost:27017/"


@app.route('/add_ingredient', methods=['POST'])
def add_ingredient():
    ingredient_data = {
        'name': request.json.get('name'),
        'reference': request.json.get('reference'),
        'category': request.json.get('category'),
        'supplier': request.json.get('supplier'),
        'unit_cost': request.json.get('unit_cost'),
        'stock_quantity': request.json.get('stock_quantity')
    }
    ingredients_collection.insert_one(ingredient_data)
    return 'Ingrédient ajouté avec succès', 201


# Routes pour différentes pages
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/index1')
def index1():
    return render_template('index1.html')
    
    
@app.route('/recettes')
def recettes():
    return render_template('recettes.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/stocks')
def stocks():
    return render_template('stocks.html')


@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html')

    
@app.route('/edit_ingredient', methods=['POST'])
def edit_ingredient():
    ingredient_id = request.form.get('ingredient_id')

    # Redirigez l'utilisateur vers la page des ingrédients après l'édition
    return redirect('/ingredients')


@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

# calendar
events = []  # Liste pour stocker des événements de calendrier
class Event(Resource):
    def get(self, event_id):
        if event := events_collection.find_one({'id': event_id}):
            return event, 200
        else:
            return "Événement non trouvé", 404

    def post(self):
        new_event = request.get_json()
        events.append(new_event)
        return new_event, 201


api.add_resource(Event, "/event", "/event/<string:event_id>")


@app.route('/get_product_image', methods=['GET'])
def get_product_image():
    barcode = request.args.get('barcode')
    if not barcode:
        return "Veuillez fournir un code-barres", 400

    product_data = food_api.fetch_product(barcode)
    if not product_data or 'image_url' not in product_data:
        return "Produit non trouvé ou image indisponible", 404

    return product_data['image_url'], 200






if __name__ == '__main__':
    app.run(debug=True)
