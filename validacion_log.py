from datetime import datetime
import os

ubi_actual = os.path.dirname(os.path.abspath(__file__))

ruta_log = os.path.join(ubi_actual, "logs", "log.txt")

def validar_salidas(df_inv):
    if (df_inv["Inventario"] < df_inv["Salida"]).any():
        guardar_log("No hay suficientes inventarios")
        raise ValueError("No hay suficientes inventarios")

def guardar_log(mensaje):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ruta_log, "a", encoding="utf-8") as l:
        l.write(f"{fecha} {mensaje}\n")
