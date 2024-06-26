from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:
    schema = 'esquema_dojos_y_ninjas'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #Una lista con todos los ninjas de un dojo
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL(cls.schema).query_db(query)
        '''results is a list of dictionaries
        results = [
            {
                "id": 1,
                "name": "PYTHON",
                "created_at": "2021-07-20 16:00:00",
                "updated_at": "2021-07-20 16:00:00"
            },
            {
                "id": 2,
                "name": "JAVA",
                "created_at": "2021-07-20 16:00:00",
                "updated_at": "2021-07-20 16:00:00"
            }
        '''
        dojos = []
    
        for row in results:
            # row is a dictionary, for example: row = {"id": 1, "name": "Coding Dojo", "created_at": "2021-07-20 16:00:00", "updated_at": "2021-07-20 16:00:00"}
            dojos.append(cls(row))
        print(f"Ultimo Dojo: {dojos[int(len(dojos)) - 1].name}")

        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(cls.schema).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id=%(id)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)
        if results:
            dojo = cls(results[0])
            for row in results:
                row_data = {
                    "id": row['id'],
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "age": row['age'],
                    "created_at": row['created_at'],
                    "updated_at": row['updated_at'],
                    "dojo_id": row['dojo_id']
                }
                dojo.ninjas.append(Ninja(row_data))
            return dojo
        else:
            return None
