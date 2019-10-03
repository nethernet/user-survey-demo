from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/user_db'
application.config['SQLALCHEMY_ECHO'] = True
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)
