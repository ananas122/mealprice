from flask import Flask, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook

app = Flask(__name__)

# Configuration OAuth pour Google
google_bp = make_google_blueprint(client_id='YOUR_GOOGLE_CLIENT_ID',
                                   client_secret='YOUR_GOOGLE_CLIENT_SECRET',
                                   redirect_to='google_login')
app.register_blueprint(google_bp, url_prefix='/google_login')

# Configuration OAuth pour Facebook
facebook_bp = make_facebook_blueprint(client_id='YOUR_FACEBOOK_CLIENT_ID',
                                       client_secret='YOUR_FACEBOOK_CLIENT_SECRET',
                                       redirect_to='facebook_login')
app.register_blueprint(facebook_bp, url_prefix='/facebook_login')

# Clé secrète de session Flask
app.secret_key = 'votre_clé_secrète'

# Page de connexion
@app.route('/login')
def login():
    if not google.authorized and not facebook.authorized:
        return "Veuillez vous connecter avec Google ou Facebook."
    return redirect(url_for('home'))

# Page d'accueil
@app.route('/')
def home():
    if google.authorized:
        resp = google.get('/plus/v1/people/me')
        assert resp.ok, resp.text
        return 'Connecté avec Google: ' + resp.json()['displayName']
    elif facebook.authorized:
        resp = facebook.get('/me?fields=id,name,email')
        assert resp.ok, resp.text
        return 'Connecté avec Facebook: ' + resp.json()['name']
    else:
        return 'Connectez-vous avec Google ou Facebook'


if __name__ == '__main__':
    app.run(debug=True)
