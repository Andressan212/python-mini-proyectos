from faker import Faker
import pandas as pd
import random
from datetime import datetime

fake = Faker("es_AR")

# cantidades
CANT_CLIENTES = 50
CANT_PRODUCTOS = 80
CANT_VENTAS = 200

# --------------------------
# GENERAR CLIENTES
# --------------------------
def generar_clientes(n):
    clientes = []
    for i in range(1, n + 1):
        cliente = {
            "id": i,
            "nombre": fake.name(),
            "telefono": fake.phone_number(),
            "direccion": fake.address().replace("\n", ", "),
            "email": fake.email()
        }
        clientes.append(cliente)
    return clientes


# --------------------------
# GENERAR PRODUCTOS
# --------------------------
def generar_productos(n):
    productos = []

    categorias = ["Bebidas", "Lácteos", "Carnes", "Verduras", "Limpieza", "Panadería", "Golosinas"]

    for i in range(1, n + 1):
        producto = {
            "id": i,
            "nombre": fake.word().capitalize(),
            "categoria": random.choice(categorias),
            "precio": round(random.uniform(1000, 15000), 2),
            "codigo_barra": fake.ean(length=13),
            "stock": random.randint(5, 200)
        }
        productos.append(producto)

    return productos


# --------------------------
# GENERAR VENTAS
# --------------------------
def generar_ventas(n, clientes, productos):
    ventas = []
    detalle_ventas = []
    venta_id = 1

    for _ in range(n):

        cliente = random.choice(clientes)
        fecha = fake.date_time_this_year()

        venta = {
            "id_venta": venta_id,
            "id_cliente": cliente["id"],
            "fecha": fecha,
            "total": 0
        }

        total = 0
        cantidad_productos = random.randint(1, 6)

        for _ in range(cantidad_productos):
            producto = random.choice(productos)
            cantidad = random.randint(1, 5)

            subtotal = producto["precio"] * cantidad
            total += subtotal

            detalle = {
                "id_venta": venta_id,
                "id_producto": producto["id"],
                "producto": producto["nombre"],
                "cantidad": cantidad,
                "precio_unitario": producto["precio"],
                "subtotal": round(subtotal, 2)
            }

            detalle_ventas.append(detalle)

        venta["total"] = round(total, 2)
        ventas.append(venta)

        venta_id += 1

    return ventas, detalle_ventas


# --------------------------
# EXPORTAR CSV
# --------------------------
def exportar_csv(nombre, datos):
    df = pd.DataFrame(datos)
    df.to_csv(f"{nombre}.csv", index=False, encoding="utf-8-sig")
    print(f"✅ Archivo generado: {nombre}.csv")


# --------------------------
# EJECUTAR SIMULADOR
# --------------------------
clientes = generar_clientes(CANT_CLIENTES)
productos = generar_productos(CANT_PRODUCTOS)
ventas, detalle = generar_ventas(CANT_VENTAS, clientes, productos)

exportar_csv("clientes", clientes)
exportar_csv("productos", productos)
exportar_csv("ventas", ventas)
exportar_csv("detalle_ventas", detalle)

print("\n✅ SIMULACIÓN COMPLETA FINALIZADA")
print("---------------------------------")
print(f"Clientes generados: {len(clientes)}")
print(f"Productos generados: {len(productos)}")
print(f"Ventas generadas: {len(ventas)}")
print(f"Detalles de ventas: {len(detalle)}")
# instalar faker y pandas si no los tenes
# pip install faker pandas