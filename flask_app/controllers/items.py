from flask_bcrypt import Bcrypt
from flask import Flask, render_template, redirect, session, flash, request, url_for
import pymysql
from flask_app import app
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models import user
from flask_app.models import item
from flask_app.models import billing_info



@app.route('/order')
def order():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('order_view.html', items = item.Item.get_all_items())


@app.route("/order/review" , methods=['POST', 'GET'])
def order_preview():
    if 'user_id' not in session:
        return redirect('/')
    if request.method == "POST":
        description = request.form.get('description')
        price = request.form.get('price')
        return "Order details: " + description + price
    return render_template('order_view.html')


@app.route("/order/placed" , methods=['POST', 'GET'])
def order_placed():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('success.html')

    # select = request.form.get('selection')
    # print(str(select)) # just to see what select is


