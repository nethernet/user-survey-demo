from flask_sqlalchemy import SQLAlchemy
from database import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    colour = db.Column(db.String(200))
    pets = db.Column(db.String(4))

    def __init__(self, name, colour, pets):
        self.name = name
        self.colour = colour
        self.pets = pets

    def __repr__(self):
        return '<User %r>' % self.name
