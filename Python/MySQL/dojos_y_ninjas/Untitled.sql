USE esquema_usuarios;


-- Consulta: crea 3 usuarios nuevos
-- INSERT INTO users (first_name, last_name, email) VALUES ('Juan', 'Pérez', 'juan@example.com'), ('María', 'Gómez', 'maria@example.com'), ('Pedro', 'López', 'pedro@example.com');

-- Consulta: recupera todos los usuarios
-- SELECT * FROM users;

-- Consulta: recupera el primer usuario usando su dirección de correo electrónico
-- SELECT * FROM users WHERE email = 'juan@example.com' LIMIT 1;

-- Consulta: recupera el último usuario usando su id
SELECT * FROM users ORDER BY id DESC LIMIT 1;

