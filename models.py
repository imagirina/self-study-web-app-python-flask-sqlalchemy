# Data Model
from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False) # this field can not be Null
    date = db.Column(db.Date, nullable=False)

    # function represents each instance of this model
    def __repr__(self):
        return f'{self.title} created on {self.date}'