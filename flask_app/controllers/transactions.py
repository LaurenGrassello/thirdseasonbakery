from flask_bcrypt import Bcrypt
from flask import Flask, render_template, redirect, session, flash, request
from flask_app import app
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models import user
from flask_app.models import transaction
from flask_app.models import item
from flask_app.models import billing_info




"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
import stripe
# This is your test secret API key.
stripe.api_key = 'pk_test_51KYbhzBWScTJy5yL9lIkeozFzkNSrQ5boYNcqnrtnqnodpyJ7nUCOGTZvCPrianCfhlWIITUIiF68tmxnbQtSVKN00J14pRpSy'

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://localhost:5000'

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{item.price}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
            automatic_tax={'enabled': True},
        )
    except Exception as e:
        return str(e)

    return render_template('success.html', checkout_session)

