from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = environ.get("SQLALCHEMY_DATABASE_URI")
application.config['SQLALCHEMY_ECHO'] = True
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)
