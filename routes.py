from app import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
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
        
        flash('Task added to database')

        # once we added data to db, instead of rendering 'about.html', we redirect url_for('index.html')
        # return render_template('about.html', form=form, title=form.title.data)

        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = Task.query.get(task_id)
    # print(task)
    form = forms.AddTaskForm()

    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash('Task has been updated')
            return redirect(url_for('index'))
        form.title.data = task.title
        return render_template('edit.html', form=form, task_id=task_id)
    else:
        flash('Task not found')
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    task = Task.query.get(task_id)
    form = forms.DeleteTaskForm()

    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash('Task has been deleted')
            return redirect(url_for('index'))
        return render_template('delete.html', form=form, task_id=task_id, title=task.title)
    else:
        flash('Task not found')
    return redirect(url_for('index'))