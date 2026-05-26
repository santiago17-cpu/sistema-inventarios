
def validar_salidas(df_inv):
    if (df_inv["Inventario"] < df_inv["Salida"]).any():
        raise ValueError("No hay suficientes inventarios")

def procesar_movimientos(df_inv):
    #restar las salidas
    df_inv["Inventario"] = df_inv["Inventario"] - df_inv["Salida"]
    
    # sumar las entradas 
    df_inv["Inventario"] = df_inv["Inventario"] + df_inv["Entrada"]
    
    #limpiar la entrada y salida
    df_inv["Salida"] = 0 
    df_inv["Entrada"] = 0
    
    # definiendo el estado dependiendo de la cantidad que halla en el inventario
    df_inv["Estado"] = "estable"
    df_inv.loc[df_inv["Inventario"] <= df_inv["Umbral"], "Estado"] = "Bajo"
    return df_inv
    
    
def detectar_bajos(df_inv):
    bajos = df_inv[df_inv["Estado"] == "Bajo"]
    return bajos
