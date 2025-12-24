-- ==========================================
-- 1. CREACIÓN DE LA BASE DE DATOS Y TABLAS
-- ==========================================
CREATE DATABASE IF NOT EXISTS gestion_academica;
USE gestion_academica;

-- 1. Tabla Departamento (Entidad Independiente)
CREATE TABLE IF NOT EXISTS departamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ubicacion VARCHAR(100)
);

-- 2. Tabla Profesor (Relación 1:M con Departamento)
CREATE TABLE IF NOT EXISTS profesores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    especialidad VARCHAR(100),
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

-- 3. Tabla Estudiante (Relación 1:M con Departamento)
CREATE TABLE IF NOT EXISTS estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    fecha_ingreso DATE,
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

-- 4. Tabla Curso (Catálogo de materias - Independiente o vinculada a Dept)
CREATE TABLE IF NOT EXISTS cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    creditos INT
);

-- 5. Tabla Clase (La instancia real: Un Curso dictado por un Profesor en un periodo)
-- Relación 1:M con Curso y 1:M con Profesor
CREATE TABLE IF NOT EXISTS clases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    curso_id INT,
    profesor_id INT,
    periodo VARCHAR(20), -- Ej: "2024-Q1"
    FOREIGN KEY (curso_id) REFERENCES cursos(id),
    FOREIGN KEY (profesor_id) REFERENCES profesores(id)
);

-- 6. Tabla Inscripción (Relación M:M resuelta entre Estudiante y Clase)
CREATE TABLE IF NOT EXISTS inscripciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estudiante_id INT,
    clase_id INT,
    fecha_inscripcion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
    FOREIGN KEY (clase_id) REFERENCES clases(id)
);

-- 7. Tabla Calificación (Detalle de la nota de una inscripción)
CREATE TABLE IF NOT EXISTS calificaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    inscripcion_id INT,
    tipo_evaluacion VARCHAR(50), -- Ej: Parcial, Final, Proyecto
    nota DECIMAL(5, 2),
    FOREIGN KEY (inscripcion_id) REFERENCES inscripciones(id) ON DELETE CASCADE
);

-- ==========================================
-- 2. INSERCIÓN DE DATOS (CRUD: INSERT)
-- ==========================================

-- Insertar Departamentos
INSERT INTO departamentos (nombre, ubicacion) VALUES 
('Ingeniería de Sistemas', 'Edificio A'),
('Arquitectura', 'Edificio B'),
('Medicina', 'Edificio C');

-- Insertar Profesores
INSERT INTO profesores (nombre, especialidad, departamento_id) VALUES 
('Ing. Nedual Vargas', 'Redes y Seguridad', 1),
('Arq. Maria Lopez', 'Urbanismo', 2),
('Dr. House', 'Diagnóstico', 3);

-- Insertar Estudiantes
INSERT INTO estudiantes (nombre, email, fecha_ingreso, departamento_id) VALUES 
('Juan Perez', 'juan@email.com', '2023-01-15', 1),
('Ana Gomez', 'ana@email.com', '2023-01-20', 1),
('Luis Diaz', 'luis@email.com', '2023-02-10', 2);

-- Insertar Cursos (Materias)
INSERT INTO cursos (titulo, creditos) VALUES 
('Base de Datos Avanzada', 4),
('Diseño Urbano', 5),
('Anatomía I', 6);

-- Insertar Clases (Abriendo secciones)
-- El Ing. Nedual da Base de Datos en el periodo 2024-Q1
INSERT INTO clases (curso_id, profesor_id, periodo) VALUES (1, 1, '2024-Q1');
-- La Arq. Maria da Diseño Urbano
INSERT INTO clases (curso_id, profesor_id, periodo) VALUES (2, 2, '2024-Q1');

-- Insertar Inscripciones
-- Juan y Ana se inscriben en Base de Datos (Clase ID 1)
INSERT INTO inscripciones (estudiante_id, clase_id) VALUES (1, 1), (2, 1);
-- Luis se inscribe en Diseño Urbano (Clase ID 2)
INSERT INTO inscripciones (estudiante_id, clase_id) VALUES (3, 2);

-- Insertar Calificaciones
-- Notas para Juan en Base de Datos (Inscripcion 1)
INSERT INTO calificaciones (inscripcion_id, tipo_evaluacion, nota) VALUES 
(1, 'Parcial 1', 85.5),
(1, 'Proyecto Final', 90.0);

-- Notas para Ana en Base de Datos (Inscripcion 2)
INSERT INTO calificaciones (inscripcion_id, tipo_evaluacion, nota) VALUES 
(2, 'Parcial 1', 70.0),
(2, 'Proyecto Final', 100.0);

-- ==========================================
-- 3. CONSULTAS Y JOINS
-- ==========================================

-- A. Ver lista de estudiantes y sus departamentos
SELECT e.nombre AS Estudiante, d.nombre AS Carrera
FROM estudiantes e
JOIN departamentos d ON e.departamento_id = d.id;

-- B. Ver qué materias está dando cada profesor
SELECT p.nombre AS Profesor, c.titulo AS Curso_Impartido, cl.periodo
FROM clases cl
JOIN profesores p ON cl.profesor_id = p.id
JOIN cursos c ON cl.curso_id = c.id;

-- C. Reporte completo de Notas (Estudiante - Materia - Nota)
SELECT e.nombre AS Estudiante, c.titulo AS Materia, cal.tipo_evaluacion, cal.nota
FROM calificaciones cal
JOIN inscripciones i ON cal.inscripcion_id = i.id
JOIN estudiantes e ON i.estudiante_id = e.id
JOIN clases cl ON i.clase_id = cl.id
JOIN cursos c ON cl.curso_id = c.id;

-- ==========================================
-- 4. ESTADÍSTICAS
-- ==========================================

-- A. Promedio de notas por Estudiante
SELECT e.nombre, AVG(cal.nota) AS Promedio_General
FROM calificaciones cal
JOIN inscripciones i ON cal.inscripcion_id = i.id
JOIN estudiantes e ON i.estudiante_id = e.id
GROUP BY e.nombre;

-- B. Cantidad de estudiantes por Departamento
SELECT d.nombre, COUNT(e.id) AS Total_Estudiantes
FROM departamentos d
LEFT JOIN estudiantes e ON d.id = e.departamento_id
GROUP BY d.nombre;

-- ==========================================
-- 5. MANIPULACIÓN DE DATOS (UPDATE / DELETE)
-- ==========================================

-- ACTUALIZAR: Subir la nota del Parcial 1 de Juan a 90
UPDATE calificaciones 
SET nota = 90.00 
WHERE inscripcion_id = 1 AND tipo_evaluacion = 'Parcial 1';

-- ELIMINAR: Borrar una calificación errónea
-- (Borramos la nota más baja de Ana)
DELETE FROM calificaciones 
WHERE id = 3; -- Asumiendo que el ID 3 es el Parcial de Ana con 70.0

-- Verificación final
SELECT * FROM calificaciones;