import os
import smtplib
from email.message import EmailMessage
import ssl

def send_email(receiver,em_subject,em_body):
    email_sender = "Sender's Email"
    email_password = 'YOUR_GOOGLE_PASSWORD_FOR_PYTHON_APP'
    email_receiver = receiver

    subject = em_subject
    body = em_body

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp :
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())