-- Desactivar el modo seguro de actualizaciones SQL
SET SQL_SAFE_UPDATES = 0;

USE esquema_libros;

-- Consulta: crea 5 usuarios diferentes
-- INSERT INTO users (first_name, last_name) VALUES ('Jane', 'Austen'), ('Emily', 'Dickinson'), ('Fyodor', 'Dostoevsky'), ('William', 'Shakespeare'), ('Lau', 'Tzu');

-- Consulta: crea 5 libros con los siguientes nombres y número de páginas
-- INSERT INTO books (tittle, num_of_pages) VALUES ('C Sharp', 300), ('Java', 400), ('Python', 350), ('PHP', 320), ('Ruby', 380);

-- Consulta: cambia el nombre del libro de C Sharp a C#
-- UPDATE books SET tittle = 'C#' WHERE tittle = 'C Sharp';

-- Consulta: cambia el nombre del cuarto usuario a Bill
-- UPDATE users SET first_name = 'Bill' WHERE id = 4;

-- Consulta: haz que el primer usuario marque como favorito los 2 primeros libros
-- INSERT INTO favorites (user_id, book_id) VALUES (1, 1), (1, 2);

