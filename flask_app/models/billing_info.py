from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import Flask, flash
from flask_app.controllers import items
from flask_app.controllers import billings_info
from flask_app.controllers import users
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)




class Billing:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.street_address = data['street_address']
        self.city = data['city']
        self.state = data['state']
        self.zip_code = data['zip_code']
        self.creditcard_number = data['creditcard_number']
        self.creditcard_type = data['creditcard_type']
        self.creditcard_exp = data['creditcard_exp']
        self.creditcard_cvv = data['creditcard_cvv']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod
    def add_payment(cls,data):
        cc_list=['1234 5678 1234 5678',
                '1234567812345678',
                '1234-5678-1234-5678',
                '1234-5678-1234-56786',
                '1234-55678-1234-5678']
        pattern = '^([0-9]{4}[- ]?){3}[0-9]{4}$'
        for eachnumber in cc_list:
            result = re.match(pattern, eachnumber)
        if result:
            print(eachnumber+" is a valid credit card number.")
        else:
            print(eachnumber+" is an invalid credit card number.")
        billing_info = {
            "street_address": data["street_address"],
            "city": data["city"],
            "state": data["state"],
            "zip_code": data["zip_code"],
            "creditcard_number": data["credticard_number"],
            "creditcard_type": data["creditcard_type"],
            "creditcard_exp": data["creditcard_exp"],
            "creditcard_cvv": data["creditcard_cvv"],
            "created_at": data["created_at"],
            "updated_at": data["updated_at"]
        }
        query = "INSERT INTO billing_info (street_address, city, state, zip_code, creditcard_number, creditcard_type, creditcard_exp, creditcard_cvv, created_at) " \
        "VALUES (%(street_address)s, %(city)s, %(state)s, %(zip_code)s, %(creditcard_number)s, %(creditcard_type)s, %(creditcard_exp)s, %(creditcard_cvv)s,  NOW())"
        return connectToMySQL("belt_exam_2_schema").query_db(query, billing_info, cc_list)
    


    @staticmethod
    def validate_payment(data):
        is_valid = True 
        if len(data['street_address']) < 4:
            flash("Street address must be at least 4 characters.", "payment")
            is_valid = False
        if len(data['city']) < 2:
            flash("City must be at least 2 characters.", "payment")
            is_valid = False
        if len(data['state']) ==2:
            flash("Please enter state abbreviation", "payment")
            is_valid = False
        if len(data['zip_code']) < 5:
            flash("Zip code must be at least 5 characters", "payment")
            is_valid = False
            flash("Creditcard number must be at least 16 characters.", "payment")
            is_valid = False
        if len(data['creditcard_exp']) < 16:
            flash("", "payment")
            is_valid = False
        if len(data['creditcard_cvv']) < 3:
            flash("Creditcard cvv must be at least 3 characters.", "payment")
            is_valid = False
        
        return is_valid
