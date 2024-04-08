from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.email= data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query= "SELECT * FROM users;"
        result= connectToMySQL('email_validation_schema').query_db(query)
        users=[]
        for user in result:
            users.append(cls(user))
        return users
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users (  email  ) VALUES (  %(email)s );"
        return connectToMySQL('email_validation_schema').query_db( query, data )
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = (%(id)s);"
        return connectToMySQL('email_validation_schema').query_db(query, data)
    

    @staticmethod
    def validate_user(user):
        is_valid = True
        # Test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Dirección de correo electrónico inválida!")
            is_valid = False
        elif len(user['email'].split('@')[0]) < 6:
            flash("La primera parte del correo electrónico debe tener al menos 6 caracteres antes del '@'")
            is_valid = False

        for email in User.get_all():
            if user['email'] == email.email:
                flash("Este correo electrónico ya está en uso")
                is_valid = False

        return is_valid

    # @staticmethod
    # def validate_user( user ):
    #     is_valid = True
    #     # test whether a field matches the pattern
    #     if not EMAIL_REGEX.match(user['email']): 
    #         flash("Invalid email address!")
    #         is_valid = False
    #     for email in User.get_all():
    #         if user['email']== email.email:
    #             flash("This email is taken")
    #             is_valid= False
    #     return is_valid