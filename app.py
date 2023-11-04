from flask import Flask
from handlers.routes import configure_routes
from flask_cors import CORS
import pymysql  # Import PyMySQL
from dotenv import load_dotenv
from flask_session import Session
import os
from supabase import create_client, Client

load_dotenv()

app = Flask(__name__)

configure_routes(app)

CORS(app)

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_USE_SIGNER'] = True
app.config['SECRET_KEY'] = 'ananasma'
Session(app)

# Configure your MySQL connection using PyMySQL - Local SQL database connection
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = os.getenv('mp_db')


# Create a PyMySQL connection
# mysql = pymysql.connect(
#   host=app.config['MYSQL_HOST'],
#    user=app.config['MYSQL_USER'],
#    password=app.config['MYSQL_PASSWORD'],
#    db=app.config['MYSQL_DB']
# )


# Supabase configuration
# SUPABASE_URL
url = "https://phkrkssbltpeowygwtvz.supabase.co"
# SUPABASE_KEY
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBoa3Jrc3NibHRwZW93eWd3dHZ6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTkwNTg5NDcsImV4cCI6MjAxNDYzNDk0N30.3wZg6O36smQV972LOU_fL6RpQPoCihC5shkaBTLaFSc"
supabase = create_client(url, key)

if __name__ == '__main__':
    app.run(debug=True)
