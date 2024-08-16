import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists('env.py'):
    import env
    
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)

from taskmanager import routes
