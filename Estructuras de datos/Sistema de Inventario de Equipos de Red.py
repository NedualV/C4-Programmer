import ipaddress # Biblioteca para validar direcciones IP
from datetime import datetime # Biblioteca para poner fecha a las alertas

# --- ESTRUCTURAS DE DATOS ---

# Vectores (Listas unidimensionales)
nombres_equipos = [] 
ubicaciones = []

# Matriz (Lista de listas)
# Estructura de cada fila: [Tipo, IP, Estado]
matriz_datos = [] 

# --- FUNCIONES ---

def registrar_equipo():
    print("\n--- REGISTRAR NUEVO EQUIPO ---")
    nombre = input("Nombre del equipo (ej. Switch-Core): ")
    tipo = input("Tipo (ej. Router, Switch, AP): ")
    ubicacion = input("Ubicación (ej. Rack 1, Piso 2): ")
    
    # Validación de IP usando la biblioteca ipaddress
    while True:
        ip_str = input("Dirección IP (ej. 192.168.1.1): ")
        try:
            # Esto verificará si la IP es válida (IPv4)
            ip_obj = ipaddress.ip_address(ip_str)
            break
        except ValueError:
            print("Error: Formato de IP inválido. Intente de nuevo.")

    # Validación de estado
    print("Seleccione estado: 1. Activo | 2. Inactivo | 3. Mantenimiento")
    opcion_estado = input("Opción: ")
    if opcion_estado == "1":
        estado = "Activo"
    elif opcion_estado == "2":
        estado = "Inactivo"
    else:
        estado = "Mantenimiento"

    # Guardar en Vectores
    nombres_equipos.append(nombre)
    ubicaciones.append(ubicacion)
    
    # Guardar en Matriz [Tipo, IP, Estado]
    fila_datos = [tipo, ip_str, estado]
    matriz_datos.append(fila_datos)
    
    print(f"¡Equipo {nombre} registrado con éxito!")

def mostrar_inventario():
    print("\n--- INVENTARIO GENERAL ---")
    print(f"{'NOMBRE':<15} | {'TIPO':<10} | {'IP':<15} | {'UBICACIÓN':<15} | {'ESTADO'}")
    print("-" * 75)
    
    # Usamos un bucle for con range y len para recorrer los vectores y la matriz en paralelo
    total_equipos = len(nombres_equipos)
    
    for i in range(total_equipos):
        # Extraemos datos de los vectores
        nombre = nombres_equipos[i]
        ubicacion = ubicaciones[i]
        
        # Extraemos datos de la matriz (fila i)
        tipo = matriz_datos[i][0]
        ip = matriz_datos[i][1]
        estado = matriz_datos[i][2]
        
        print(f"{nombre:<15} | {tipo:<10} | {ip:<15} | {ubicacion:<15} | {estado}")

def generar_alertas():
    print("\n--- ALERTAS DEL SISTEMA ---")
    hay_alertas = False
    hora_actual = datetime.now().strftime("%H:%M:%S")
    
    total_equipos = len(nombres_equipos)
    
    for i in range(total_equipos):
        # Revisamos la columna 2 de la matriz (Estado)
        estado_actual = matriz_datos[i][2]
        
        if estado_actual == "Inactivo" or estado_actual == "Mantenimiento":
            nombre = nombres_equipos[i]
            ip = matriz_datos[i][1]
            print(f"[ALERTA {hora_actual}] El equipo '{nombre}' ({ip}) está: {estado_actual.upper()}")
            hay_alertas = True
            
    if not hay_alertas:
        print("No hay alertas. Todos los sistemas operativos.")

# --- BLOQUE PRINCIPAL (MENÚ) ---

def menu_principal():
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE RED ===")
        print("1. Registrar Equipo")
        print("2. Ver Inventario")
        print("3. Generar Reporte de Alertas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_equipo()
        elif opcion == "2":
            if len(nombres_equipos) > 0:
                mostrar_inventario()
            else:
                print("\nInventario vacío.")
        elif opcion == "3":
            if len(nombres_equipos) > 0:
                generar_alertas()
            else:
                print("\nNo hay equipos para auditar.")
        elif opcion == "4":
            print("Cerrando sistema...")
            break
        else:
            print("Opción no válida.")

# Ejecutar el programa
menu_principal()