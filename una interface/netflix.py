import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Datos simulados de películas
peliculas = [
    {"titulo": "Stranger Things", "imagen": "stranger.jpg"},
    {"titulo": "The Witcher", "imagen": "witcher.jpg"},
    {"titulo": "Breaking Bad", "imagen": "breaking.jpg"},
]

def buscar():
    texto = buscador.get().lower()
    resultados = [p for p in peliculas if texto in p["titulo"].lower()]
    mostrar_peliculas(resultados)

def mostrar_peliculas(lista):
    for widget in frame_peliculas.winfo_children():
        widget.destroy()
    
    for p in lista:
        try:
            img = Image.open(p["imagen"])
            img = img.resize((120, 180))
            img_tk = ImageTk.PhotoImage(img)
        except:
            img_tk = None
        
        btn = tk.Button(frame_peliculas, text=p["titulo"], image=img_tk, compound="top",
                        command=lambda t=p["titulo"]: reproducir(t))
        btn.image = img_tk
        btn.pack(side="left", padx=10)

def reproducir(titulo):
    messagebox.showinfo("Reproduciendo", f"Ahora reproduciendo: {titulo}")

# Ventana principal
root = tk.Tk()
root.title("Mi Netflix")
root.geometry("800x400")
root.config(bg="black")

# Buscador
buscador = tk.Entry(root, width=30, font=("Arial", 14))
buscador.pack(pady=10)
btn_buscar = tk.Button(root, text="Buscar", command=buscar)
btn_buscar.pack(pady=5)

# Frame para películas
frame_peliculas = tk.Frame(root, bg="black")
frame_peliculas.pack(pady=20)

# Mostrar todas las películas al inicio
mostrar_peliculas(peliculas)

root.mainloop()
# installar Pillow si no está instalado:
# pip install Pillow    