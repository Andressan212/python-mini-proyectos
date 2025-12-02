import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Función para contar
def contar():
    texto = entrada_texto.get("1.0", tk.END)

    palabras = len(texto.split())
    caracteres = len(texto) - 1  # Resta el salto final
    lineas = len(texto.splitlines())

    lbl_palabras.config(text=f"Palabras: {palabras}")
    lbl_caracteres.config(text=f"Caracteres: {caracteres}")
    lbl_lineas.config(text=f"Líneas: {lineas}")

# Función para abrir archivo .txt
def abrir_archivo():
    ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])

    if ruta:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

        entrada_texto.delete("1.0", tk.END)
        entrada_texto.insert(tk.END, contenido)

# Crear ventana
ventana = tk.Tk()
ventana.title("Contador de palabras")
ventana.geometry("600x400")

# Título
titulo = ttk.Label(ventana, text="Contador de Palabras", font=("Arial", 16))
titulo.pack(pady=10)

# Caja de texto
entrada_texto = tk.Text(ventana, height=10, width=60)
entrada_texto.pack(pady=10)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5)

btn_contar = ttk.Button(frame_botones, text="Contar", command=contar)
btn_contar.grid(row=0, column=0, padx=5)

btn_abrir = ttk.Button(frame_botones, text="Abrir archivo .txt", command=abrir_archivo)
btn_abrir.grid(row=0, column=1, padx=5)

# Resultados
lbl_palabras = ttk.Label(ventana, text="Palabras: 0", font=("Arial", 12))
lbl_palabras.pack(pady=5)

lbl_caracteres = ttk.Label(ventana, text="Caracteres: 0", font=("Arial", 12))
lbl_caracteres.pack(pady=5)

lbl_lineas = ttk.Label(ventana, text="Líneas: 0", font=("Arial", 12))
lbl_lineas.pack(pady=5)

ventana.mainloop()
