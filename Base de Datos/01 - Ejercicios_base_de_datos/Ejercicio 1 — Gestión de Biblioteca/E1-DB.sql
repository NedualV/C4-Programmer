CREATE DATABASE IF NOT EXISTS biblioteca;
USE biblioteca;

-- Tabla Autores
CREATE TABLE IF NOT EXISTS autores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50)
);

-- Tabla Libros
CREATE TABLE IF NOT EXISTS libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    anio_publicacion INT,
    autor_id INT,
    FOREIGN KEY (autor_id) REFERENCES autores(id)
);

-- Insertar Datos
INSERT INTO autores (nombre, nacionalidad) VALUES 
('Gabriel García Márquez', 'Colombiana'),
('J.K. Rowling', 'Británica');

INSERT INTO libros (titulo, anio_publicacion, autor_id) VALUES 
('Cien años de soledad', 1967, 1),
('Harry Potter', 1997, 2);

-- Consulta de prueba
SELECT libros.titulo, autores.nombre 
FROM libros 
JOIN autores ON libros.autor_id = autores.id;