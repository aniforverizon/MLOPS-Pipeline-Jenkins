import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "limbachiyajeet42@gmail.com"  # Enter your address
receiver_email = "acanubhav@gmail.com"  # Enter receiver address
password = "123456789@987654321"
message = """\
Subject: Hi there

This message is sent from jenkins because your accuracy is less than 90%. Try again"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
