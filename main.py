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
    body = db.Column(db.Text) # this is the post

    def __init__(self, title, body):
        self.title = title
        self.body = body


# display individual blog entries or all blog posts

@app.route('/blog')
def display_blog_entries():
    entry_id = request.args.get('id')
    if (entry_id):
        entry = Entry.query.get(entry_id)
        return render_template('single_entry.html', title="Blog Post", entry=entry)
    else:
        # display every existing blog entry
        sort = request.args.get('sort')
        # displays newest first
        if (sort=="newest"):
            all_entries = Entry.query.order_by(Entry.created.desc()).all()
        else:
        # just shows all entries
            all_entries = Entry.query.all()
        return render_template('all_entries.html', title= "All Blog Posts", all_entries=all_entries)
        


