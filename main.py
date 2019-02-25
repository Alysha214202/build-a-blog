from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:build-a-blog@localhost:8888/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# class for the database, stores blog entries

class Entry(db.Model):

    # data that should go into columns, primary ID below
    id = db.Column(db.Integer, primary_key=True)
    # set to Text so there is not a character limit
    title = db.Column(db.Text) # this is the title
    post = db.Column(db.Text) # this is the post

    def __init__(self, title, body):
        self.title = title
        self.body = body
