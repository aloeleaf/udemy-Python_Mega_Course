import smtplib
import ssl


def send_mail_smtp(message):
    host = ""
    port = 25

    username = ""
    password = ""

    receiver = ""

    with smtplib.SMTP(host, port) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


def send_mail_smtp_ssl(message):
    host = ""
    port = 465

    username = ""
    password = ""

    receiver = ""

    context = ssl.create_default_context()

    # SSL connection
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
