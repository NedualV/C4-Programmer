CREATE DATABASE IF NOT EXISTS colegio;
USE colegio;

-- Tabla Estudiantes
CREATE TABLE IF NOT EXISTS estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT
);

-- Tabla Cursos
CREATE TABLE IF NOT EXISTS cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_curso VARCHAR(50) NOT NULL,
    profesor VARCHAR(50)
);

-- Tabla Matrículas (Tabla Intermedia)
CREATE TABLE IF NOT EXISTS matriculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estudiante_id INT,
    curso_id INT,
    fecha_inscripcion DATETIME DEFAULT CURRENT_TIMESTAMP, -- Corregido para Workbench
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

-- Insertar Datos
INSERT INTO estudiantes (nombre, edad) VALUES ('Maria Lopez', 22);
INSERT INTO cursos (nombre_curso, profesor) VALUES ('Programación', 'Ing. Perez');

-- Maria se inscribe en Programación
INSERT INTO matriculas (estudiante_id, curso_id) VALUES (1, 1);

-- Consulta de Matrículas
SELECT e.nombre AS Estudiante, c.nombre_curso AS Materia, m.fecha_inscripcion
FROM matriculas m
JOIN estudiantes e ON m.estudiante_id = e.id
JOIN cursos c ON m.curso_id = c.id;