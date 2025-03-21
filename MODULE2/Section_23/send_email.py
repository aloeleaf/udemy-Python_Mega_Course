import smtplib, ssl

def send_mail(message):
    host = ""
    port = 25  


    # username = ""
    # password = ""

    username = ""
    password = ""

    receiver = ""
    #context = ssl.create_default_context()


    
    with smtplib.SMTP(host, port) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message )

    ## SSL connection
    # with smtplib.SMTP_SSL(host, port) as server:
    #     server.login(username, password)
    #     server.sendmail(username, receiver, message )