import tkinter as tk

def agregar(valor):
    entrada.insert(tk.END, valor)

def limpiar():
    entrada.delete(0, tk.END)

def borrar_uno():
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual[:-1])

def calcular():
    try:
        resultado = eval(entrada.get())
        limpiar()
        entrada.insert(0, str(resultado))
    except:
        limpiar()
        entrada.insert(0, "Error")

ventana = tk.Tk()
ventana.title("Calculadora PRO")
ventana.geometry("380x520")
ventana.config(bg="#1e1e1e")
ventana.resizable(False, False)

entrada = tk.Entry(
    ventana,
    font=("Arial", 22),
    bd=10,
    relief="sunken",
    justify="right",
    bg="white"
)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=10, sticky="nsew")

botones = [
    ("C", limpiar), ("⌫", borrar_uno), ("%", lambda: agregar("%")), ("/", lambda: agregar("/")),
    ("7", lambda: agregar("7")), ("8", lambda: agregar("8")), ("9", lambda: agregar("9")), ("*", lambda: agregar("*")),
    ("4", lambda: agregar("4")), ("5", lambda: agregar("5")), ("6", lambda: agregar("6")), ("-", lambda: agregar("-")),
    ("1", lambda: agregar("1")), ("2", lambda: agregar("2")), ("3", lambda: agregar("3")), ("+", lambda: agregar("+")),
    ("0", lambda: agregar("0")), (".", lambda: agregar(".")), ("(", lambda: agregar("(")), (")", lambda: agregar(")")),
]

fila = 1
col = 0

for texto, comando in botones:
    boton = tk.Button(
        ventana,
        text=texto,
        width=6,
        height=2,
        font=("Arial", 16),
        bg="#2e2e2e",
        fg="white",
        activebackground="#444",
        activeforeground="white",
        command=comando
    )
    boton.grid(row=fila, column=col, padx=8, pady=8, sticky="nsew")

    col += 1
    if col > 3:
        col = 0
        fila += 1

btn_igual = tk.Button(
    ventana,
    text="=",
    font=("Arial", 18, "bold"),
    bg="#00ff99",
    fg="black",
    height=2,
    command=calcular
)

btn_igual.grid(row=fila, column=0, columnspan=4, padx=8, pady=15, sticky="nsew")

# Ajuste de columnas y filas
for i in range(4):
    ventana.columnconfigure(i, weight=1)

for i in range(fila + 1):
    ventana.rowconfigure(i, weight=1)

ventana.mainloop()
