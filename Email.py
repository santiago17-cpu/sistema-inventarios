#conectarme al serividor de gmail
import smtplib
#crear el contenido del gmail
from email.message import EmailMessage
from validacion_log import guardar_log

def Enviar_email(bajos):
    remitente = "bot.personal.santiago.0@gmail.com"
    contraseña = "shla nowz lmoz iann"
    destinatario = "santiago777cornejo@gmail.com"
    
    #creando el contenido del msg
    msg = EmailMessage()
    msg["subject"] = "Reporte automatico"
    msg["From"] = remitente
    msg["to"] = destinatario
    
    texto ="Hola Santiago ALERTA DE PRODUCTOS BAJOS.\n\n"
    
    for _, fila in bajos.iterrows():
        texto += f"{fila['Producto']} - {fila['Inventario']} - {fila['Estado']}\n"
    
    msg.set_content(texto)
    # conectando con servidor de gmail
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(remitente, contraseña)
        smtp.send_message(msg)
    guardar_log("gmail enviado")