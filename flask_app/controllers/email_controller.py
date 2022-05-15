from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.email_model import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods= (['POST']))
def submit():
    data = {
        'email':request.form['email']
    }
    if not User.validate_user(request.form):
        return redirect('/')
    User.save(data)
    return redirect('/success')

@app.route('/success')
def success():
    emails= User.get_all()
    lastEmail = User.get_last()
    print(lastEmail)

    return render_template('success.html', emails=emails, lastEmail = lastEmail)

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id' : id
    }
    User.deleteThis(data)
    return redirect('/success')
