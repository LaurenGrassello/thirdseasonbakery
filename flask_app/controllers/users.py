from flask_bcrypt import Bcrypt
from flask import Flask, render_template, redirect, session, flash, request
from flask_app import app
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models import user
from flask_app.models.user import User



# main page with nav to menu/place order/contact
@app.route('/')
def bakery_home():
    return render_template('index.html')

# dashboard displaying user login/reg page
@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return redirect('/order')
    return render_template('login.html')


# action to register new user
@app.route('/register', methods=['POST'])
def user_reg():
    if not user.User.validate_user(request.form):
        return redirect('/dashboard')
    session ['user_id'] = user.User.new_user(request.form)
    return redirect("/order")


# action for user login
@app.route('/login', methods=['POST'])
def login():
    if not user.User.validate_email(request.form):
        return redirect('/dashboard')
    user_sessions = user.User.select_email(request.form)
    session['user_id'] = user_sessions.id
    return redirect('/order')



# logout action to clear session**WORKS
@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')