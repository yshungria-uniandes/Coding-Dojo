
from flask_app.config.mysqlconnection import connectToMySQL

class Restaurant:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # Creamos una lista para que luego podamos agregar todas las hamburguesas que están asociadas a un restaurante
        self.burgers = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO restaurants (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('burgers').query_db(query, data)
