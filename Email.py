#conectarme al serividor de gmail
import smtplib
#crear el contenido del gmail
from email.message import EmailMessage
from validacion_log import guardar_log
import os
from dotenv import load_dotenv
load_dotenv


def Enviar_email(bajos, destinatario):
    remitente_env = os.getenv("REMITENTE")
    contraseña_env = os.getenv("CONTRASENA")
    destinatario_env = destinatario
    
    #creando el contenido del msg
    msg = EmailMessage()
    msg["subject"] = "Reporte automatico"
    msg["From"] = remitente_env
    msg["to"] = destinatario_env
    
    texto ="ALERTA DE PRODUCTOS BAJOS.\n\n"
    
    for _, fila in bajos.iterrows():
        texto += f"{fila['Producto']} - {fila['Inventario']} - {fila['Estado']}\n"
    
    msg.set_content(texto)
    # conectando con servidor de gmail
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(remitente_env, contraseña_env)
        smtp.send_message(msg)
    guardar_log("gmail enviado")
