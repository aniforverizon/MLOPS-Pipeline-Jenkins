import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "#############@gmail.com"  # Enter your address
receiver_email = "##########@gmail.com"  # Enter receiver address
password = "##############"
message = """\
Subject: Hi there

This message is sent from jenkins because your accuracy is less than 90%. Try again"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
