from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)

# Créez une connexion à la base de données SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Assurez-vous que la table "ingredients" existe dans la base de données
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        reference TEXT NOT NULL,
        category TEXT,
        supplier TEXT,
        unit_cost REAL,
        stock_quantity REAL
    )
''')
conn.commit()


@app.route('/add_ingredient', methods=['POST'])
def add_ingredient():
    name = request.json.get('name')
    reference = request.json.get('reference')
    category = request.json.get('category')
    supplier = request.json.get('supplier')
    unit_cost = request.json.get('unit_cost')
    stock_quantity = request.json.get('stock_quantity')

    # Insérez les données dans la table "ingredients"
    cursor.execute('''
        INSERT INTO ingredients (name, reference, category, supplier, unit_cost, stock_quantity)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, reference, category, supplier, unit_cost, stock_quantity))
    conn.commit()

    return 'Ingrédient ajouté avec succès', 201

# Routes pour différentes pages
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
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
    # Code pour récupérer la liste des ingrédients depuis la base de données
    # et afficher la page HTML des ingrédients
    return render_template('ingredients.html')
@app.route('/edit_ingredient', methods=['POST'])
def edit_ingredient():
    ingredient_id = request.form.get('ingredient_id')
    # Récupérez les détails de l'ingrédient à partir de la base de données en utilisant l'ID
    # Effectuez les modifications nécessaires

    # Redirigez l'utilisateur vers la page des ingrédients après l'édition
    return redirect('/ingredients')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')




if __name__ == '__main__':
    app.run(debug=True)
