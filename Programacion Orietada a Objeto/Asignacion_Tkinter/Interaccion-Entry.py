import tkinter as tk

def mostrar_texto():
    texto = entry.get()  # Obtener texto del Entry
    lbl_resultado.config(text=f"Escribiste: {texto}") # Actualizar Label

root = tk.Tk()
root.title("Ejercicio 2: Entry y Button")
root.geometry("300x150")

# Campo de entrada
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Botón
btn = tk.Button(root, text="Mostrar Texto", command=mostrar_texto)
btn.pack(pady=5)

# Etiqueta para el resultado
lbl_resultado = tk.Label(root, text="")
lbl_resultado.pack(pady=10)

root.mainloop()