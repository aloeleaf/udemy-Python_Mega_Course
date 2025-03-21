import smtplib, ssl

host = "mail.bkt.birosag.hu"
port = 25  
#port = 465  

# username = "szabolcs.sandor@gmail.com"
# password = "bdwnhqycxpaiihdj"

username = "helpdesk"
password = "gj/29BF37."

receiver = "sandorsz@birosag.hu"
context = ssl.create_default_context()

message = """\
Subject: Hi there
This message is sent from Python.
"""


with smtplib.SMTP_SSL(host, port, ) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message )