from datetime import datetime

def validar_salidas(df_inv):
    if (df_inv["Inventario"] < df_inv["Salida"]).any():
        guardar_log("No hay suficientes inventarios")
        raise ValueError("No hay suficientes inventarios")

def guardar_log(mensaje):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("Gestion de inventarios/logs/log.txt", "a", encoding="utf-8") as l:
        l.write(f"{fecha} {mensaje}\n")
