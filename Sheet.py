#conectarese con speadsheets API
import gspread
#conectar con drive API
from google.oauth2.service_account import Credentials
import pandas as pd
from validacion_log import guardar_log
import os
import json
from dotenv import load_dotenv
permisos =[
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
load_dotenv()
credenciales_json = os.getenv("GOOGLE_CREDENTIALS")
credenciales_dict = json.loads(credenciales_json)
credenciales = Credentials.from_service_account_info(credenciales_dict, scopes= permisos)


cliente = gspread.authorize(credenciales)

def abrir_spreadsheets(cliente, usuario):
    sheets = cliente.open_by_key(usuario)
    hoja_inventario = sheets.worksheet("Inventario")
    inventario = hoja_inventario.get_all_records()  

    df_inv = pd.DataFrame(inventario)
        #guardar_log("Iniciando proceso")
    print(df_inv)
    return df_inv, hoja_inventario
    
    
def actualizar_sheets(df_inv, hoja):
    columnas = df_inv[["Inventario", "Entrada", "Salida", "Umbral", "Estado"]]
    hoja.update(columnas.values.tolist(), "B2")
    guardar_log("Actualización completa")

