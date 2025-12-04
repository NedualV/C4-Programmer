import tkinter as tk

# Creo la ventana principal
root = tk.Tk()
root.title("Ejercicio 1: Bienvenida")
root.geometry("300x100")

# Creo y empaquetor la etiqueta
label = tk.Label(root, text="¡Ta facil el Tkinter!", font=("Arial", 14))
label.pack(pady=30)  # pady añade espacio vertical

# Iniciar el bucle de la aplicación
root.mainloop()