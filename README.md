# 🚀 Fundamentos de Programación, Python, C++ y Bases de Datos

Este repositorio consolida mi portafolio de aprendizaje progresivo, abarcando desde la lógica algorítmica fundamental hasta el desarrollo de aplicaciones de escritorio con persistencia de datos y programación de bajo nivel.

El proyecto se divide en cuatro áreas clave:
1.  **Lógica Algorítmica** (PSeInt).
2.  **Desarrollo de Software** (Python + POO + GUI).
3.  **Ingeniería de Datos** (Modelado SQL y Consultas Avanzadas).
4.  **Programación Estructurada** (C++ Essentials - Cisco).

---

## 🏆 Proyecto Destacado: Sistema de Gestión de Red e Inventario

Aplicación de escritorio completa para la administración de activos de infraestructura TI. Este proyecto integra todos los conocimientos adquiridos (Frontend, Backend y Base de Datos).

* **Tecnologías:** Python 3, Tkinter, MySQL Connector, Librería `ipaddress`.
* **Funcionalidades:**
    * ✅ **CRUD Completo:** Registro, lectura y búsqueda de equipos (Routers, Switches, PCs).
    * ✅ **Validación de Datos:** Verificación estricta de direcciones IP y tipos de datos.
    * ✅ **Alertas Inteligentes:** Sistema automático que detecta y notifica equipos en estado "Inactivo" o "Mantenimiento".
    * ✅ **Persistencia:** Almacenamiento robusto en base de datos relacional (MySQL).

---

## 🧩 Contenido del Repositorio

### 1. PSeInt (Fundamentos)
Ejercicios de lógica pura enfocados en el pensamiento estructurado.
* **Tipos de Datos y Operadores:** Aritmética, lógica booleana y manipulación de cadenas.
* **Estructuras de Control:** Condicionales anidados y bucles (`Para`, `Mientras`).

### 2. Python (Scripting y POO)
Transición a código de producción con sintaxis moderna.
* **Programación Orientada a Objetos (POO):** Clases, Herencia y Polimorfismo (Ej: Modelos de `Usuario`, `Vehiculo`, `Coche`).
* **Interfaces Gráficas (GUI):** Desarrollo de ventanas interactivas con **Tkinter** (Calculadoras, Formularios, Canvas).
* **Manejo de Errores:** Uso de bloques `try/except` para aplicaciones robustas.

### 3. Bases de Datos y SQL
Diseño de esquemas relacionales y manipulación avanzada de datos.
* **Modelado:** Relaciones Uno a Muchos y Muchos a Muchos (Ej: Sistema de Biblioteca y Ventas).
* **Consultas Avanzadas (Queries):**
    * Uso de `JOIN` para vincular tablas (Estudiantes - Departamentos).
    * Funciones de agregación (`COUNT`, `AVG`, `MAX`).
    * Filtrado avanzado con `GROUP BY` y `HAVING`.
    * Ingeniería inversa y diagramado.

### 4. C++ (Cisco Networking Academy - Essentials 1)
Incorporación de conceptos de programación de bajo nivel, gestión de memoria y sintaxis estricta.
* **Fundamentos:** Sintaxis, semántica, compilación y tipos de datos primitivos.
* **Control de Flujo:** Estructuras condicionales complejas (`switch`, `if-else`) y bucles iterativos.
* **Vectores y Arreglos:** Manipulación y recorrido de colecciones de datos.
* **Modularización:** Uso de funciones y paso de parámetros por valor.

---

## ⚙️ Instalación y Uso

Para ejecutar el **Sistema de Inventario**, sigue estos pasos:

1.  **Requisitos Previos:**
    * Tener instalado Python 3.x.
    * Tener un servidor MySQL activo (XAMPP, WAMP o MySQL Server).

2.  **Instalar dependencias:**
    Ejecuta el siguiente comando en tu terminal para instalar el conector de base de datos:
    ```bash
    pip install mysql-connector-python
    ```

3.  **Configurar la Base de Datos:**
    * Abre tu gestor SQL (phpMyAdmin o Workbench).
    * Importa o ejecuta el script `base_datos.sql` (ubicado en la carpeta `db` o raíz).
    * *Opcional:* Si tu MySQL tiene contraseña, edita el archivo `.py` en la función `conectar_db()`.

4.  **Ejecutar la App:**
    ```bash
    python Inventario_de_red.py
    ```

---

## 🛠️ Guía de Solución de Problemas

* **Error `ModuleNotFoundError`:** Asegúrate de haber ejecutado el comando `pip install` del paso 2.
* **Error de Conexión DB:** Verifica que XAMPP/MySQL esté encendido y que el usuario/contraseña en el script de Python coincidan con los de tu servidor local.
* **PSeInt no ejecuta:** Revisa que los bloques `FinSi` o `FinProceso` estén correctamente cerrados.

---

## 📚 Autor

**NEDUAL E. VARGAS PEREZ**

*Entusiasta de la Infraestructura TI, Ciberseguridad y Desarrollo de Software.*
*Explorando la intersección entre la administración de redes, la automatización con Python y la eficiencia de C++.*
