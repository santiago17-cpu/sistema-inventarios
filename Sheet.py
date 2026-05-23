#conectarese con speadsheets API
import gspread
#conectar con drive API
from google.oauth2.service_account import Credentials
import pandas as pd
from validacion_log import guardar_log

ruta = r"C:\Users\santi\OneDrive\Escritorio\Proyectos py\Gestion de inventarios\sistema-de-inventario.json"
permisos =[
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
credenciales = Credentials.from_service_account_file(ruta, scopes= permisos)

cliente = gspread.authorize(credenciales)

def abrir_spreadsheets(cliente):
    sheets = cliente.open("Sistema de inventario")
    hoja_inventario = sheets.worksheet("Inventario")
    inventario = hoja_inventario.get_all_records()  

    df_inv = pd.DataFrame(inventario)
    guardar_log("Iniciando proceso")
    return df_inv, hoja_inventario
    
    
def actualizar_sheets(df_inv, hoja):
    columnas = df_inv[["Inventario", "Entrada", "Salida", "Umbral", "Estado"]]
    hoja.update(columnas.values.tolist(), "B2")
    guardar_log("Actualización completa")
