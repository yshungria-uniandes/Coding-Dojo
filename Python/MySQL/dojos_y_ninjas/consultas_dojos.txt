-- Desactivar el modo seguro de actualizaciones SQL
SET SQL_SAFE_UPDATES = 0;

-- Usar la base de datos esquema_dojos_y_ninjas
USE esquema_dojos_y_ninjas;

-- Crear 3 nuevos dojos
INSERT INTO dojos (name, created_at, updated_at) VALUES ('Dojo 1', NOW(), NOW()), ('Dojo 2', NOW(), NOW()), ('Dojo 3', NOW(), NOW());

-- Eliminar los 3 dojos que acabas de crear
DELETE FROM dojos WHERE id BETWEEN 1 AND 3;

-- Crear 3 dojos adicionales
INSERT INTO dojos (name, created_at, updated_at) VALUES ('Dojo 4', NOW(), NOW()), ('Dojo 5', NOW(), NOW()), ('Dojo 6', NOW(), NOW());

-- Crear 3 ninjas que pertenezcan al primer dojo
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) SELECT 'Ninja 1', 'Apellido 1', 25, NOW(), NOW(), id FROM dojos ORDER BY id LIMIT 1;
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) SELECT 'Ninja 2', 'Apellido 2', 28, NOW(), NOW(), id FROM dojos ORDER BY id LIMIT 1;
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) SELECT 'Ninja 3', 'Apellido 3', 30, NOW(), NOW(), id FROM dojos ORDER BY id LIMIT 1;

-- Crear 3 ninjas que pertenezcan al segundo dojo
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) SELECT 'Ninja 4', 'Apellido 4', 22, NOW(), NOW(), id FROM dojos ORDER BY id LIMIT 1, 1;
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) SELECT 'Ninja 5', 'Apellido 5', 26, NOW(), NOW(), id FROM dojos ORDER BY id LIMIT 1, 1;
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) SELECT 'Ninja 6', 'Apellido 6', 29, NOW(), NOW(), id FROM dojos ORDER BY id LIMIT 1, 1;

-- Crear 3 ninjas que pertenezcan al tercer dojo
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) SELECT 'Ninja 7', 'Apellido 7', 24, NOW(), NOW(), id FROM dojos ORDER BY id DESC LIMIT 1;
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) SELECT 'Ninja 8', 'Apellido 8', 27, NOW(), NOW(), id FROM dojos ORDER BY id DESC LIMIT 1;
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) SELECT 'Ninja 9', 'Apellido 9', 31, NOW(), NOW(), id FROM dojos ORDER BY id DESC LIMIT 1;

-- Recuperar todos los ninjas del primer dojo
SELECT * FROM ninjas WHERE dojo_id = (SELECT id FROM dojos ORDER BY id LIMIT 1);

-- Recuperar todos los ninjas del último dojo
SELECT * FROM ninjas WHERE dojo_id = (SELECT id FROM dojos ORDER BY id DESC LIMIT 1);

-- Recuperar el dojo del último ninja
SELECT dojos.* FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id ORDER BY ninjas.id DESC LIMIT 1;

SELECT * FROM dojos;
SELECT * FROM ninjas