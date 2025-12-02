import tkinter as tk
from tkinter import messagebox

# Datos simulados de películas por categoría
peliculas = {
    "Populares": ["Stranger Things", "The Witcher", "Breaking Bad", "Dark", "Narcos", "Money Heist", "Lucifer"],
    "Comedia": ["Brooklyn Nine-Nine", "The Office", "Friends", "How I Met Your Mother"],
    "Drama": ["The Crown", "13 Reasons Why", "Ozark", "Euphoria"],
}

def reproducir(titulo):
    messagebox.showinfo("Reproduciendo", f"Ahora reproduciendo: {titulo}")

def mostrar_categoria(categoria):
    # Limpiar el frame antes de mostrar
    for widget in frame_peliculas.winfo_children():
        widget.destroy()
    
    # Crear un canvas con scroll horizontal
    canvas = tk.Canvas(frame_peliculas, height=120, bg="black")
    canvas.pack(side="top", fill="x", expand=True)

    scrollbar = tk.Scrollbar(frame_peliculas, orient="horizontal", command=canvas.xview)
    scrollbar.pack(side="bottom", fill="x")
    canvas.configure(xscrollcommand=scrollbar.set)

    inner_frame = tk.Frame(canvas, bg="black")
    canvas.create_window((0,0), window=inner_frame, anchor="nw")

    # Agregar botones de películas
    for titulo in peliculas[categoria]:
        btn = tk.Button(inner_frame, text=titulo, width=20, height=5, bg="red", fg="white",
                        font=("Arial", 10, "bold"), command=lambda t=titulo: reproducir(t))
        btn.pack(side="left", padx=5, pady=10)

    inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def buscar():
    texto = buscador.get().lower()
    resultados = []
    for cat in peliculas:
        for titulo in peliculas[cat]:
            if texto in titulo.lower():
                resultados.append(titulo)
    
    # Mostrar resultados como una categoría temporal
    peliculas["Resultados"] = resultados
    mostrar_categoria("Resultados")

# Ventana principal
root = tk.Tk()
root.title("Mi Netflix")
root.geometry("800x400")
root.config(bg="black")

# Buscador
buscador = tk.Entry(root, width=30, font=("Arial", 14))
buscador.pack(pady=10)
btn_buscar = tk.Button(root, text="Buscar", command=buscar, bg="red", fg="white")
btn_buscar.pack(pady=5)

# Frame para categorías y películas
frame_categorias = tk.Frame(root, bg="black")
frame_categorias.pack(pady=10)

frame_peliculas = tk.Frame(root, bg="black")
frame_peliculas.pack(fill="x")

# Botones de categorías
for cat in peliculas.keys():
    btn_cat = tk.Button(frame_categorias, text=cat, bg="gray20", fg="white",
                        font=("Arial", 12, "bold"),
                        command=lambda c=cat: mostrar_categoria(c))
    btn_cat.pack(side="left", padx=5)

# Mostrar primera categoría al inicio
mostrar_categoria(list(peliculas.keys())[0])

root.mainloop()

# estar Pillow si no está instalado:
# pip install Pillow
#la ezquizofrenia me consumen :v
