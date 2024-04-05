from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

db = 'books_schema'

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # create
    @classmethod
    def create(cls, data):
        try:
            query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
            return connectToMySQL(db).query_db(query, data)
        except Exception as e:
            print(f"Error al crear un nuevo autor: {str(e)}")
            return False
    
    @classmethod
    def add_favorite(cls, data):
        try:
            query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
            return connectToMySQL(db).query_db(query, data)
        except Exception as e:
            print(f"Error al agregar un libro favorito: {str(e)}")
            return False

    # read
    @classmethod
    def get_all(cls):
        try:
            query = "SELECT * FROM authors;"
            results = connectToMySQL(db).query_db(query)
            all_authors = [cls(author) for author in results]
            return all_authors
        except Exception as e:
            print(f"Error al obtener la lista de autores: {str(e)}")
            return []

    @classmethod
    def get_one(cls, data):
        try:
            query = "SELECT * FROM authors WHERE id = %(id)s;"
            print(f"Running Query: {query}")
            results = connectToMySQL(db).query_db(query, data)
            if results:
                return cls(results[0])
            return None
        except Exception as e:
            print(f"Error al obtener la información del autor: {str(e)}")
            return None
    
    @classmethod
    def get_favorites(cls, data):
        try:
            query = "SELECT books.* FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
            print(f"Running Query: {query}")
            results = connectToMySQL(db).query_db(query, data)
            fav_books = [book.Book(row) for row in results]
            return fav_books
        except Exception as e:
            print(f"Error al obtener los libros favoritos del autor: {str(e)}")
            return []

    # update
    @classmethod
    def update(cls, data):
        try:
            query = "UPDATE authors SET name = %(name)s WHERE id = %(id)s;"
            return connectToMySQL(db).query_db(query, data)
        except Exception as e:
            print(f"Error al actualizar el nombre del autor: {str(e)}")
            return False
    
    # delete
    @classmethod
    def delete(cls, data):
        try:
            query = "DELETE FROM authors WHERE id = %(id)s;"
            return connectToMySQL(db).query_db(query, data)
        except Exception as e:
            print(f"Error al eliminar el autor: {str(e)}")
            return False
