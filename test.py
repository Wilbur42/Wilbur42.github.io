
import smtplib
import socket
from email.message import EmailMessage

comp_name = socket.gethostname()
msg = EmailMessage()
msg['Subject'] = 'Web Response'
msg['From'] = 'will008ward@gmail.com'
msg['To'] = 'will008ward@gmail.com'

file_data = []
file_data.append(socket.gethostname())
file_data.append(socket.gethostbyname(socket.gethostname()))

#msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename='Comp Data')
msg.set_content(f'{file_data}')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('will008ward@gmail.com', 'Pa33w0rd')
    smtp.send_message(msg)

print('Process Complete')
