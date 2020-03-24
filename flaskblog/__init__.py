from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Secret key for security reasons
app.config['SECRET_KEY']='55fa2e959fe1a080993499098c6650c3bb'
# applicable for SQL lite database *a simple file on HDD*
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Create Database instance
db = SQLAlchemy(app)

from flaskblog import routes
