import smtplib

def send_mail(title, body):
    """Use this methos to sendo email, for this, pass the title and body information in entry.
    Obs.: Configure variables below according your email server.
    """
    smtp_server = 'smtp.gmail.com'
    smtp_server_port = '587'
    email_login = 'login@gmail.com'
    email_password = 'email_password'
    email_from = 'from@gmail.com'
    email_send = 'send@gmail.com'

    message = str(body).encode('utf-8').strip()
    server_connection = smtplib.SMTP(smtp_server, smtp_server_port)
    server_connection.connect(smtp_server, smtp_server_port)
    server_connection.ehlo()
    server_connection.starttls()
    server_connection.ehlo()
    server_connection.login(email_login, email_password)
    server_connection.sendmail(email_from, email_send, message) 
    server_connection.quit()