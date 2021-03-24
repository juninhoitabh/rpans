import smtplib
# import pyautogui as p
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from dotenv import load_dotenv # Configuração das variaveis de ambient
import os #manipular variaveis de ambiente

def enviaEmail(destinatario, assunto, mensagem):
    load_dotenv()
    host = os.getenv("HOST")
    port = 587
    user = os.getenv("MAIL_USER")
    password = os.getenv("PASS_EMAIL")     # Criando objeto
    # print('Criando objeto servidor...')
    server = smtplib.SMTP(host, port)

    # Login com servidor
    # print('Login...')
    server.ehlo()
    server.starttls()
    server.login(user, password)


    # Criando mensagem
    message = str(mensagem)
    # print('Criando mensagem...')
    email_msg = MIMEMultipart()
    email_msg['From'] = user
    email_msg['To'] = str(destinatario)
    email_msg['Subject'] = str(assunto)
    email_msg.attach(MIMEText(message))
    # Adicionando imagem Anexo
    with open('imagens/telaErro.png', 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename="telaErro.png")
        email_msg.attach(img)
    # print('Adicionando texto...')
    # Enviando mensagem
    # print('Enviando mensagem...')
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    # print('Mensagem enviada!')
    server.quit()
    return()
