import tkinter as tk

# Variables para guardar la última posición del mouse
last_x, last_y = None, None

def activar_dibujo(event):
    # Guardamos la posición inicial al hacer clic
    global last_x, last_y
    last_x, last_y = event.x, event.y

def dibujar(event):
    global last_x, last_y
    # Dibujamos una línea desde la última posición hasta la actual
    canvas.create_line(last_x, last_y, event.x, event.y, width=2, fill="black")
    # Actualizamos la última posición
    last_x, last_y = event.x, event.y

root = tk.Tk()
root.title("Ejercicio 5: Pizarra de Dibujo")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

# Eventos del mouse
canvas.bind('<Button-1>', activar_dibujo)  # Click inicial
canvas.bind('<B1-Motion>', dibujar)        # Mover manteniendo presionado

# Botón para borrar
btn_borrar = tk.Button(root, text="Borrar Todo", command=lambda: canvas.delete("all"))
btn_borrar.pack(pady=5)

root.mainloop()