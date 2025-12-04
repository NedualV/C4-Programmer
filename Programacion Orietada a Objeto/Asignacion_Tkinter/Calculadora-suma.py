import tkinter as tk

def sumar():
    try:
        # Se combierte el texto a número
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = num1 + num2
        lbl_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        lbl_resultado.config(text="Error: Ingresa solo números")

root = tk.Tk()
root.title("Ejercicio 3: Sumadora")
root.geometry("300x200")

tk.Label(root, text="Número 1:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Número 2:").pack()
entry2 = tk.Entry(root)
entry2.pack()

btn_sumar = tk.Button(root, text="Sumar", command=sumar)
btn_sumar.pack(pady=10)

lbl_resultado = tk.Label(root, text="Resultado: 0", font=("Arial", 12, "bold"))
lbl_resultado.pack()

root.mainloop()