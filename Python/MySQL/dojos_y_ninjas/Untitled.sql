-- Desactivar el modo seguro de actualizaciones SQL
SET SQL_SAFE_UPDATES = 0;

USE esquema_amistades;

-- Consulta: crea 6 usuarios nuevos
-- INSERT INTO users (first_name, last_name) VALUES ('Amy', 'Giver'), ('Eli', 'Byers'), ('Big', 'Bird'), ('La rana', 'René'), ('Marky', 'Mark'), ('La rana', 'René');

-- Consulta: haz que el usuario 1 sea amigo del usuario 2, 4 y 6
-- INSERT INTO friendships (user_id, friend_id) VALUES (1, 2), (1, 4), (1, 6);

-- Consulta: haz que el usuario 2 sea amigo del usuario 1, 3 y 5
-- INSERT INTO friendships (user_id, friend_id) VALUES (2, 1), (2, 3), (2, 5);


-- Consulta: haz que el usuario 3 sea amigo del usuario 2 y 5
-- INSERT INTO friendships (user_id, friend_id) VALUES (3, 2), (3, 5);

-- Consulta: haz que el usuario 4 sea amigo del usuario 3
-- INSERT INTO friendships (user_id, friend_id) VALUES (4, 3);

-- Consulta: haz que el usuario 5 sea amigo del usuario 1 y 6
-- INSERT INTO friendships (user_id, friend_id) VALUES (5, 1), (5, 6);

-- Consulta: haz que el usuario 6 sea amigo del usuario 2 y 3
INSERT INTO friendships (user_id, friend_id) VALUES (6, 2), (6, 3);
