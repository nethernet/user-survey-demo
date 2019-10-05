from flask import Flask, render_template, flash, request, redirect, url_for
from wtforms import validators, StringField
from wtforms.validators import InputRequired
from os import urandom
from flask_wtf import FlaskForm
from models import Users
from database import application, db

application.config['SECRET_KEY'] = urandom(24)

class UserForm(FlaskForm):
    first_name = StringField('first name', validators=[InputRequired()])
    colour = StringField('favourite colour', validators=[InputRequired()])
    pets = StringField('cats or dogs', validators=[InputRequired()])

@application.route("/", methods=["GET","POST"])
def user_survey():
    db.create_all()
    db.session.commit()

    form = UserForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            name = request.form['first_name']
            existing_user = Users.query.filter(Users.name == name).first()
            if existing_user:
                flash('Error: User {} already exists'.format(name))
            else:
                user = Users(request.form['first_name'], request.form['colour'], request.form['pets'])
                db.session.add(user)
                db.session.commit()
                flash('Added user {} to database'.format(name))
        else:
            flash('Error: All Fields are Required')

        return redirect(url_for('user_survey'))

    return render_template('index.html', form = form, users = Users.query.all())
    

@application.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title = '404'), 404

if __name__ == "__main__":
    application.run()
