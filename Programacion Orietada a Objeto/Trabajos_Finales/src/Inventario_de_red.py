import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import ipaddress

# ==========================================
# CONFIGURACIÓN DE LA BASE DE DATOS
# ==========================================

def conectar_db():
    """Establece la conexión con la base de datos MySQL"""
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",            # Tu usuario de MySQL
            password="",            # <--- PON TU CONTRASEÑA AQUÍ SI TIENES (ej: "123456")
            database="inventario_red"
        )
        return conexion
    except mysql.connector.Error as err:
        messagebox.showerror("Error de Conexión", f"No se pudo conectar a la Base de Datos.\n\nError: {err}\n\nVerifica que XAMPP/MySQL esté encendido.")
        return None

# ==========================================
# CLASE PRINCIPAL DE LA INTERFAZ
# ==========================================

class SistemaInventario:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Red e Inventario")
        self.root.geometry("1000x650")
        self.root.configure(bg="#f0f0f0") # Color de fondo suave

        # --- VARIABLES DE CONTROL (Para capturar lo que escribe el usuario) ---
        self.var_id = tk.StringVar()
        self.var_nombre = tk.StringVar()
        self.var_tipo = tk.StringVar()
        self.var_ubicacion = tk.StringVar()
        self.var_ip = tk.StringVar()
        self.var_estado = tk.StringVar(value="Activo")

        # ==========================================
        # 1. SECCIÓN DE REGISTRO (FORMULARIO)
        # ==========================================
        frame_registro = tk.LabelFrame(self.root, text="Registrar Nuevo Equipo", font=("Arial", 10, "bold"), bg="white", padx=20, pady=20)
        frame_registro.pack(fill="x", padx=15, pady=10)

        # Fila 1: Nombre y Tipo
        tk.Label(frame_registro, text="Nombre del Equipo:", bg="white").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(frame_registro, textvariable=self.var_nombre, width=25).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_registro, text="Tipo (Router/Switch/PC):", bg="white").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        tk.Entry(frame_registro, textvariable=self.var_tipo, width=25).grid(row=0, column=3, padx=5, pady=5)

        # Fila 2: Ubicación y IP
        tk.Label(frame_registro, text="Ubicación Física:", bg="white").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(frame_registro, textvariable=self.var_ubicacion, width=25).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_registro, text="Dirección IP:", bg="white").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        tk.Entry(frame_registro, textvariable=self.var_ip, width=25).grid(row=1, column=3, padx=5, pady=5)

        # Fila 3: Estado y Botón Guardar
        tk.Label(frame_registro, text="Estado Actual:", bg="white").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        combo_estado = ttk.Combobox(frame_registro, textvariable=self.var_estado, values=["Activo", "Inactivo", "Mantenimiento"], state="readonly", width=22)
        combo_estado.grid(row=2, column=1, padx=5, pady=5)
        combo_estado.current(0)

        btn_guardar = tk.Button(frame_registro, text="💾 Guardar Equipo", command=self.guardar_equipo, bg="#28a745", fg="white", font=("Arial", 9, "bold"), cursor="hand2")
        btn_guardar.grid(row=2, column=3, sticky="ew", padx=5, pady=10)

        # ==========================================
        # 2. SECCIÓN DE CONTROL (BUSCAR Y ALERTAS)
        # ==========================================
        frame_acciones = tk.Frame(self.root, bg="#f0f0f0")
        frame_acciones.pack(fill="x", padx=15, pady=5)

        # Buscador
        tk.Label(frame_acciones, text="Buscar por ID:", bg="#f0f0f0").pack(side="left", padx=5)
        tk.Entry(frame_acciones, textvariable=self.var_id, width=10).pack(side="left", padx=5)
        tk.Button(frame_acciones, text="🔍 Buscar", command=self.buscar_por_id).pack(side="left", padx=5)
        tk.Button(frame_acciones, text="🔄 Ver Todos", command=self.cargar_datos).pack(side="left", padx=5)
        
        # Botón de Alertas (A la derecha)
        tk.Button(frame_acciones, text="⚠️ VERIFICAR ALERTAS", command=self.generar_alertas, bg="#dc3545", fg="white", font=("Arial", 9, "bold")).pack(side="right", padx=5)

        # ==========================================
        # 3. TABLA DE DATOS (TREEVIEW)
        # ==========================================
        frame_tabla = tk.Frame(self.root)
        frame_tabla.pack(fill="both", expand=True, padx=15, pady=10)

        # Configurar columnas
        columnas = ("ID", "Nombre", "Tipo", "Ubicacion", "IP", "Estado")
        self.tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        
        # Encabezados
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre Equipo")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Ubicacion", text="Ubicación")
        self.tree.heading("IP", text="Dirección IP")
        self.tree.heading("Estado", text="Estado")

        # Tamaño de columnas
        self.tree.column("ID", width=40, anchor="center")
        self.tree.column("Nombre", width=180)
        self.tree.column("Tipo", width=100)
        self.tree.column("Ubicacion", width=150)
        self.tree.column("IP", width=120)
        self.tree.column("Estado", width=100, anchor="center")

        # Barra de desplazamiento (Scrollbar)
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)

        # Cargar datos al iniciar la app
        self.cargar_datos()

    # ==========================================
    # LÓGICA DEL SISTEMA (FUNCIONES)
    # ==========================================

    def guardar_equipo(self):
        """Valida datos y guarda en MySQL"""
        nombre = self.var_nombre.get()
        tipo = self.var_tipo.get()
        ubicacion = self.var_ubicacion.get()
        ip_str = self.var_ip.get()
        estado = self.var_estado.get()

        # 1. Validaciones básicas
        if not nombre or not tipo or not ip_str:
            messagebox.showwarning("Faltan Datos", "Por favor, completa al menos Nombre, Tipo e IP.")
            return

        # 2. Validación estricta de IP (Librería ipaddress)
        try:
            ipaddress.ip_address(ip_str)
        except ValueError:
            messagebox.showerror("IP Inválida", "El formato de la dirección IP es incorrecto.\nEjemplo válido: 192.168.1.1")
            return

        # 3. Insertar en Base de Datos
        conexion = conectar_db()
        if conexion:
            cursor = conexion.cursor()
            sql = "INSERT INTO equipos (nombre, tipo, ubicacion, ip, estado) VALUES (%s, %s, %s, %s, %s)"
            val = (nombre, tipo, ubicacion, ip_str, estado)
            
            try:
                cursor.execute(sql, val)
                conexion.commit() # Guardar cambios
                messagebox.showinfo("Éxito", f"El equipo '{nombre}' ha sido registrado.")
                self.limpiar_campos()
                self.cargar_datos() # Recargar tabla
            except mysql.connector.Error as err:
                messagebox.showerror("Error SQL", f"No se pudo guardar: {err}")
            finally:
                conexion.close()

    def cargar_datos(self):
        """Lee todos los datos de MySQL y los pone en la tabla"""
        # Limpiar tabla visual
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        conexion = conectar_db()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, tipo, ubicacion, ip, estado FROM equipos ORDER BY id DESC")
            resultados = cursor.fetchall()
            
            for row in resultados:
                self.tree.insert("", "end", values=row)
            
            conexion.close()

    def buscar_por_id(self):
        """Busca un equipo específico por su ID"""
        id_buscado = self.var_id.get()
        if not id_buscado.isdigit():
            messagebox.showwarning("Error", "El ID debe ser un número.")
            return

        for fila in self.tree.get_children():
            self.tree.delete(fila)

        conexion = conectar_db()
        if conexion:
            cursor = conexion.cursor()
            sql = "SELECT id, nombre, tipo, ubicacion, ip, estado FROM equipos WHERE id = %s"
            cursor.execute(sql, (id_buscado,))
            resultado = cursor.fetchone() # Trae solo uno
            
            if resultado:
                self.tree.insert("", "end", values=resultado)
            else:
                messagebox.showinfo("Búsqueda", "No se encontró ningún equipo con ese ID.")
                self.cargar_datos() # Volver a mostrar todos
            
            conexion.close()

    def generar_alertas(self):
        """Busca equipos caídos y lanza alerta"""
        conexion = conectar_db()
        if conexion:
            cursor = conexion.cursor()
            # Buscar equipos que NO estén activos
            sql = "SELECT nombre, ip, estado FROM equipos WHERE estado != 'Activo'"
            cursor.execute(sql)
            problemas = cursor.fetchall()
            conexion.close()

            if problemas:
                mensaje = f"¡ALERTA DE SEGURIDAD!\nSe han detectado {len(problemas)} equipos con problemas:\n\n"
                for nombre, ip, estado in problemas:
                    mensaje += f"• {nombre} ({ip}) -> {estado.upper()}\n"
                
                messagebox.showwarning("Reporte de Alertas", mensaje)
            else:
                messagebox.showinfo("Sistema Seguro", "Todos los equipos están operando correctamente (Activos).")

    def limpiar_campos(self):
        self.var_nombre.set("")
        self.var_tipo.set("")
        self.var_ubicacion.set("")
        self.var_ip.set("")
        self.var_estado.set("Activo")
        self.var_nombre.set("") # Enfocar cursor (opcional, necesita binding)

# ==========================================
# INICIO DEL PROGRAMA
# ==========================================
if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = SistemaInventario(ventana_principal)
    ventana_principal.mainloop()