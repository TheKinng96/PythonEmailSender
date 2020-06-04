import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'your_name'
email['to'] = 'target_email_address'
email['subject'] = 'Hi there This is a Test Mail'

email.set_content(html.substitute({'name': 'hoyi'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your_email_here', 'your_password_here')
    smtp.send_message(email)
    print('all good boss!')