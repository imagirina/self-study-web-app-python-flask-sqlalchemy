# Create Your First Web App with Python and Flask by Coursera Project Network

# print(__name__) # value for variable __name__ will be __main__

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # instance of Flask app
# we need to set SECRET_KEY in configuration to use cSRF (without it there will be RuntimeError)
# this key will be used to generate cSRF token
# it should come from env variables
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# by running db.create_all() at the terminal will be created data.db at the root folder


# SQLAlchemy is an object relational mapper which serves as a front end to databases
db = SQLAlchemy(app) # db instance, without models yet


# after the app was instantiate, we import everything from routes.py
from routes import *

if __name__ == '__main__': # checking if app.py executed from command line
    app.run(debug=True) # we run function run() on that instance and give debug functionality to Flask

# the server reloads any time when we safe our app.py (if the code isn't finished but saved, there could be Error Messages in cmd)