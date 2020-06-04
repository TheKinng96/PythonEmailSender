import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'your_name'
email['to'] = 'target_here_email'
email['subject'] = 'Hi there This is a Test Mail'

email.set_content('hihi, hellllo')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your_email', 'your_password')
    smtp.send_message(email)
    print('all good boss!')