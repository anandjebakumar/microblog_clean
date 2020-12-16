from flask import current_app as app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Anand'
    }
    john = {
        'username': 'John'
    }
    susan = {
        'username': 'Susan'
    }
    posts = [
        {
            'author': john,
            'body': 'Beautiful day in Portland'
        },
        {
            'author': susan,
            'body': 'The avengers movie was so cool'
        }
    ]
    return render_template('index.html',title='Home',user=user,posts=posts)