import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



def conectar_email(email,otp):
    server = "smtp.gmail.com"
    port = 587
    username = "equipe18pucpr@gmail.com"
    password = "ebmtydbgptahxpnj"

    mail_from = "equipe18pucpr@gmail.com"
    mail_to = email
    mail_subject = "Segurança da Tecnologia da Informação"
    mail_body = "Olá, seu codigo: " + str(otp)

    mensagem = MIMEMultipart()
    mensagem['From'] = mail_from
    mensagem['To'] = mail_to
    mensagem['Subject'] = mail_subject
    mensagem.attach(MIMEText(mail_body, 'plain'))

    connection = smtplib.SMTP(server, port)
    connection.starttls()
    connection.login(username,password)
    connection.send_message(mensagem)
    connection.quit()