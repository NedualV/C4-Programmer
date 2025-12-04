import tkinter as tk

def agregar_elemento():
    elemento = entry_item.get()
    if elemento: 
        listbox.insert(tk.END, elemento) 
        entry_item.delete(0, tk.END) 

root = tk.Tk()
root.title("Ejercicio 4: Lista Dinámica")
root.geometry("300x300")


entry_item = tk.Entry(root, width=30)
entry_item.pack(pady=5)

btn_add = tk.Button(root, text="Agregar a la lista", command=agregar_elemento)
btn_add.pack(pady=5)


listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10, padx=10)

root.mainloop()