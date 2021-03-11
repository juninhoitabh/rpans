import smtplib
# import pyautogui as p
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Configuração


def enviaEmail(destinatario, assunto, mensagem):

    host = 'mail.nsabor.com.br'
    port = 587
    user = 'teknisa@nsabor.com.br'
    password = 'Tek1648'

    # Criando objeto
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
    with open('telaErro.png', 'rb') as fp:
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
