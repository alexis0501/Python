from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
import re 

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
#user class info
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #grab email
    @classmethod
    def get_user_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('recipes_db').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    #user id
    @classmethod
    def get_user_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('recipes_db').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    #save data
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) \
        VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW());"
        return connectToMySQL('recipes_db').query_db(query,data)
    #reg valid
    @staticmethod
    def register_validation(user):
        is_valid = True
        
        if len(user['first_name']) < 2:
            flash('First name needs to be 2 characters minimum')
            is_valid = False

        if len(user['last_name']) < 2:
            flash('Last name needs to be 2 characters minimum')
            is_valid = False
        #email valid
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(user['email']):
            flash('Email Address Invalid')
            is_valid = False
        else:
            if User.get_user_by_email({'email': user['email']}):
                flash('Email Address taken')
                is_valid = False

        if len(user['password']) < 8:
                flash('Password needs to be 8 characters minimum')
                is_valid = False
        #conf email
        if user['password'] != request.form['confirm_password']:
            flash("Passwords don't match")
            is_valid = False

        return is_valid
    #login valid
    @staticmethod
    def login_validation(user,password):
        if not user:
            flash("Invalid login")
            return False
        if not bcrypt.check_password_hash(user.password, password):
            flash("Invalid login")
            return False

        return True        