from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import Flask, flash 


class Transaction:
    def __init__(self,data):
        self.id = data['id']
        self.billing_id = data['billing_id']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']