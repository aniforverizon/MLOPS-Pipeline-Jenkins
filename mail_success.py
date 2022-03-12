import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "limbachiyajeet42@gmail.com"
receiver_email = "acanubhav@gmail.com"
password = "123456789@987654321"
message = """\
Subject: Hi there

This message is sent from jenkins.

Eureka!!!! You have achieved your desire accuracy"""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
