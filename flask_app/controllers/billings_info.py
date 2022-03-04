from flask_bcrypt import Bcrypt
from flask import Flask, render_template, redirect, session, flash, request
from flask_app import app
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models import user
from flask_app.models import item
from flask_app.models import billing_info
from authorizenet.constants import constants


@app.route('/menu')
def menu():
    return render_template('menu.html')



# @app.route('/order')
# def order():
#     if 'user_id' not in session:
#         return redirect('/')
#     return render_template('order_view.html')


# @app.route('/place/order')
# def place_order():
#     return render_template("login.html")


@app.route('/order/review', methods=['POST'])
def order_review():
    if 'user_id' not in session:
        return render_template('login.html')
    # session ['user_id'] = user.User.new_user(request.form)
    return render_template("checkout.html")


@app.route('/order/complete', methods=['POST'])
def payment_complete():
    if not user.User.validate_user(request.form):
        return redirect('/')
    session ['user_id'] = user.User.new_user(request.form)
    if not billing_info.Billing.validate_payment(request.form):
        payment = billing_info.Billing.add_payment(request.form)
    return redirect("/checkout", payment=payment)
