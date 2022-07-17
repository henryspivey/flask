from flask import render_template
from app import app 


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Henry"}
    posts = [
        {'author': {'username': 'john'},
        'body': "Beautiful day in portland"},
        {'author': {'username': 'henry'},
        'body': "He's makin' jewelry now"}
    ]
    return render_template('index.html', title=None, user=user, posts=posts)