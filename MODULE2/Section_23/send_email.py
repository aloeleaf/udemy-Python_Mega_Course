import smtplib, ssl

def send_mail(message):
    host = "mail.bkt.birosag.hu"
    port = 25  


    # username = "szabolcs.sandor@gmail.com"
    # password = "bdwnhqycxpaiihdj"

    username = "helpdesk"
    password = "gj/29BF37."

    receiver = "sandorsz@birosag.hu"
    #context = ssl.create_default_context()


    
    with smtplib.SMTP(host, port) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message )

    ## SSL connection
    # with smtplib.SMTP_SSL(host, port) as server:
    #     server.login(username, password)
    #     server.sendmail(username, receiver, message )