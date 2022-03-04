from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import Flask, flash 
from flask_app.controllers import items
from flask_app.controllers import billings_info
from flask_app.controllers import users
from flask_app.models.user import User


class Item:
    def __init__(self,data):
        self.id = data['id']
        self.description = data['description']
        self.category = data['category']
        self.price = data['price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def get_all_items(cls):
            query = "SELECT * FROM items;"
            results = connectToMySQL("third_season_schema").query_db(query)
            items = []
            for row in results:
                items.append(cls(row))
            return items



    @classmethod
    def get_all_items_and_transactions(cls):
        query = "SELECT * FROM items JOIN transactions on items.transaction_id = transactions.id;"
        results = connectToMySQL("third_season_schema").query_db(query)
        items = []
        if results:
            for row in results:
                one_item = cls(row)
                transaction_data = {
                    "id": row["transactions.id"],
                    "id": row["billing.id"],
                    "id": row["user.id"],
                    "created_at": row["transactions.created_at"],
                    "updated_at": row["transactions.updated_at"]
                }
                one_item.item = Item(transaction_data)
                items.append(one_item)
                print(one_item)
                print(items)
        return items   



    @classmethod
    def new_item(cls,data):
        query = "INSERT INTO items (transaction_id, user_id, title, description, category, price, created_at, updated_at) VALUES (%(transaction_id)s, %(user_id)s, %(title)s, %(description)s, NOW(), NOW());"
        return connectToMySQL("third_season_schema").query_db(query, data)


    @classmethod
    def select_item_id(cls,data):
        query = "SELECT * FROM items WHERE id = %(id)s"
        results = connectToMySQL("third_season_schema").query_db(query,data)
        return cls(results[0])


    @classmethod
    def create_order(cls,data):
        query = "SELECT * FROM transactions LEFT JOIN items ON transactions.id = items.transaction_id WHERE users.id = %(id)s"
        return connectToMySQL("third_season_schema").query_db(query, data)


    @classmethod
    def get_users_items(cls,data):
        query = "SELECT * FROM items JOIN users ON items.user_id = users.id WHERE user_id = %(id)s"
        results = connectToMySQL("third_season_schema").query_db(query,data)
        users_items = []
        if results:
            for row in results:
                this_item = cls(row)
                user_data = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"]
                }
                this_user = User(user_data)
                this_item.user = this_user
                users_items.append(this_item)
            print(results)
        return users_items