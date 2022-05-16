# before running make sure to turn on 'Less secure app access' for the sender_email
import smtplib
import ssl
from email.message import EmailMessage
from constants import SENDER_EMAIL
import getpass

subject = input('Enter the subject of the Email : ')
body = input('Enter the message to send (Email body) : ')
sender_email = SENDER_EMAIL
receiver_email = input('Enter the receiver email id : ')
password = getpass.getpass('Enter Password : ')

# to build the email
# initialize the EmailMessage class
message = EmailMessage()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
# message.set_content(body)

# to use html for message
html = f'''<html><body><h1>{subject}</h1><p><h3>{body}</h3></p></body></html>'''

message.add_alternative(html, subtype='html')

print('Sending Email...')
# to make a secure connection, using the ssl
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    # using the server to login to our email account to send emails
    server.login(sender_email, password)
    # as_string to convert the message object to a string and send as a string
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Sent Successfully!')
