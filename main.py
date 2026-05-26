# importamos librerias necesarias
#test deploy
from Sheet import cliente, abrir_spreadsheets, actualizar_sheets
from validacion_log import guardar_log, validar_salidas
from Procesamiento import procesar_movimientos, detectar_bajos
from Email import Enviar_email
import json
from dotenv import load_dotenv
import os
load_dotenv()

def main():       
    #with open(os.getenv("IDS"), "r", encoding="utf-8") as ids:
    ids = os.getenv("IDS")
    usuarios = json.loads(ids)
    for usuario in usuarios:
        correo = usuario["correo"]
        id_file=usuario["sheet_id"]
        df_inv, hoja = abrir_spreadsheets(cliente, id_file)
        
        validar_salidas(df_inv)
    
        df_inv = procesar_movimientos(df_inv)
    
        bajos = detectar_bajos(df_inv)
    
        try:
            Enviar_email(bajos, correo)
        
            actualizar_sheets(df_inv, hoja)        
        except Exception as e:
            guardar_log(f"Error: credenciales invalidas - actualiación cancelada {e}") 
    guardar_log("-"*30)
    
if __name__ == "__main__":
    main()

        
