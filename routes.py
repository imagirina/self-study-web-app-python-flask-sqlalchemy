from app import app, db
from flask import render_template, redirect, url_for
from models import Task
from datetime import datetime

import forms

# the decorator that we use to tell our server that at the '/' root we want to run function index()
# we can use multiple routes for the same function 
# first request after we run our server will be 127.0.0.1 - - "GET / HTTP/1.1" 200
# second - 127.0.0.1 - - "GET /index HTTP/1.1" 200 -
@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks) # by default templates exist in templates folder
    # by default Flask uses a template engine callled Jinja (it allows to use code inside HTML)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        # creating Task() object with data (we need from app import db, from models import Task)
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit() # it will save our object t in data.db
        # print('Submitted title', form.title.data) # print to the console
        
        # once we added data to db, instead of rendering 'about.html', we redirect url_for('index.html')
        # return render_template('about.html', form=form, title=form.title.data)

        return redirect(url_for('index'))
    return render_template('add.html', form=form)