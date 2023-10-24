
from flask import Flask, render_template, redirect, request, jsonify
from flask_restful import Api, Resource
from flask_mysqldb import MySQL
from datetime import datetime
from dateutil.parser import parse
from flask_cors import CORS

# Charger les variables d'environnement
from dotenv import load_dotenv
load_dotenv()
import os


app = Flask(__name__)
api = Api(app)
CORS(app)


# Configuration de la base de données MySQL en utilisant les variables d'environnement
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

# Initialisez l'extension Flask-MySQL
mysql = MySQL(app)


@app.route('/add_ingredient', methods=['POST'])
def add_ingredient():
    cur = mysql.connection.cursor()
    name = request.json.get('name')
    category = request.json.get('category')
    supplier = request.json.get('supplier')
    unit_cost = request.json.get('unit_cost')
    stock_quantity = request.json.get('stock_quantity')

    cur.execute("INSERT INTO ingredients (name, category, supplier, unit_cost, stock_quantity) VALUES (%s, %s, %s, %s, %s, %s)",
                (name, category, supplier, unit_cost, stock_quantity))
    mysql.connection.commit()
    cur.close()

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
@app.route('/api/recipes', methods=['GET'])
def fetch_recipes():
    query = request.args.get('query')
    api_key = '6820604bd3a44f849de0112f112d822e'
    url = f'https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}&query={query}'

    try:
        response = requests.get(url)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_recipe/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    # Code pour faire la requête à l'API Spoonacular ici
    # Assurez-vous de gérer les réponses de l'API correctement
    # Ensuite, renvoyez les données de la recette sous forme de JSON
    recipe_data = {
        'recipe_id': recipe_id,
        'recipe_name': 'Nom de la recette',
        'ingredients': ['Ingrédient 1', 'Ingrédient 2', 'Ingrédient 3'],
        # Autres données de recette
    }
    return jsonify(recipe_data)


@app.route('/api/recipe_details/<int:recipe_id>', methods=['GET'])
def get_recipe_details(recipe_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM recettes WHERE id=%s", [recipe_id])
    recipe = cur.fetchone()
    cur.close()

    # Convertir la recette en format JSON et la retourner
    return jsonify(recipe)


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


@app.route('/get_events', methods=['GET'])
def get_events():
    cur = mysql.connection.cursor()
    # Adaptez cette requête à votre structure de table
    cur.execute("SELECT * FROM events")
    events = cur.fetchall()
    cur.close()

    return jsonify(events), 200


@app.route('/save_event', methods=['POST'])
def save_event():
    cur = mysql.connection.cursor()
    event_data = request.json
    title = event_data.get('title')
    start_datetime = event_data.get('start_datetime')
    print(f"Title: {title}, Start Time: {start_datetime}")  # Debug log

    # Convertir la date en un objet datetime
    try:
        datetime_obj = parse(start_datetime)
    except Exception as e:
        print(f"Erreur lors de la conversion de la date: {e}")  # Debug log
        return 'Format de date invalide', 400

    # Convertir en format MySQL
    mysql_format = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

    try:
        cur.execute("INSERT INTO events (title, start_datetime) VALUES (%s, %s)",
                    (title, mysql_format))
        mysql.connection.commit()
    except Exception as e:
        # Debug log
        print(f"Erreur lors de l'insertion dans la base de données: {e}")
        return "Erreur lors de la sauvegarde de l'événement", 500

    cur.close()

    return 'Événement sauvegardé', 201



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
