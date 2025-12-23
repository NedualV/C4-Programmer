CREATE DATABASE IF NOT EXISTS ventas;
USE ventas;

-- Tabla Clientes
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100)
);

-- Tabla Productos
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);

-- Tabla Facturas (Relación Muchos a Muchos)
CREATE TABLE IF NOT EXISTS facturas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP, -- Corregido para Workbench
    cliente_id INT,
    producto_id INT,
    cantidad INT DEFAULT 1,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

-- Insertar Datos
INSERT INTO clientes (nombre, correo) VALUES ('Nedual Vargas', 'nedual@email.com');
INSERT INTO productos (nombre, precio) VALUES ('Laptop', 800.00), ('Mouse', 20.00);

-- Nedual compra una Laptop
INSERT INTO facturas (cliente_id, producto_id, cantidad) VALUES (1, 1, 1);

-- Consulta de Ventas
SELECT f.id, c.nombre, p.nombre AS producto, f.fecha 
FROM facturas f
JOIN clientes c ON f.cliente_id = c.id
JOIN productos p ON f.producto_id = p.id;