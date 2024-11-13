from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    name_env = "Wilknis"
    return render_template('index.html', name=name_env)

@app.route('/contact')
def contact():
    return render_template('contact.html')
