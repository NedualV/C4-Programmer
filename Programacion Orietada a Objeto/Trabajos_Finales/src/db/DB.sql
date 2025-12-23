-- Creación de la Base de Datos y la Tabla
CREATE DATABASE IF NOT EXISTS inventario_red;
USE inventario_red;

CREATE TABLE IF NOT EXISTS equipos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    tipo VARCHAR(30) NOT NULL,
    ubicacion VARCHAR(50),
    ip VARCHAR(15) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);