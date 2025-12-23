CREATE DATABASE IF NOT EXISTS universidad;
USE universidad;

-- Tablas
CREATE TABLE departamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50)
);

CREATE TABLE estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    fecha_nacimiento DATE,
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

CREATE TABLE profesores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    especialidad VARCHAR(50)
);

CREATE TABLE cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    profesor_id INT,
    FOREIGN KEY (profesor_id) REFERENCES profesores(id)
);

CREATE TABLE calificaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estudiante_id INT,
    curso_id INT,
    nota DECIMAL(5,2),
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

-- Datos de prueba
INSERT INTO departamentos (nombre) VALUES ('Ingeniería'), ('Artes'), ('Medicina');
INSERT INTO profesores (nombre, especialidad) VALUES ('Dr. House', 'Medicina'), ('Ing. Stark', 'Tecnología'), ('Prof. Picasso', 'Arte');
INSERT INTO cursos (nombre, profesor_id) VALUES ('Anatomía', 1), ('Robótica', 2), ('Pintura', 3), ('Programación', 2);

INSERT INTO estudiantes (nombre, apellido, fecha_nacimiento, departamento_id) VALUES 
('Juan', 'García', '2000-05-15', 1),
('Ana', 'Pérez', '1999-08-20', 3),
('Luis', 'García', '2001-01-10', 1),
('Maria', 'López', '1998-12-25', 2),
('Alberto', 'Ruiz', '2000-03-30', 1),
('Sofia', 'Mendez', '2002-07-14', 3);

INSERT INTO calificaciones (estudiante_id, curso_id, nota) VALUES 
(1, 2, 85), (1, 4, 90), -- Juan (Ingeniería)
(2, 1, 95), (2, 4, 88), -- Ana (Medicina)
(3, 2, 70), (3, 4, 65), -- Luis (Ingeniería)
(4, 3, 100),            -- Maria (Artes)
(5, 2, 92), (5, 4, 98), -- Alberto (Ingeniería)
(6, 1, 91);             -- Sofia (Medicina)