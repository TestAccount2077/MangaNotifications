import os
import sendgrid
import requests

from sendgrid.helpers.mail import *

def send_email(email, subject, body):
    
    try:
        
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

        from_email = Email("do_not_reply@herokuapp.com")
        to_email = Email(email)

        content = Content("text/plain", body)

        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        
        return True
    
    except Exception as e:
        print('Email error')
        print(e)
        return 'Email sending failed'
    
def scan_site(name, url):
    
    resp = requests.get(url)
    
    if name == 'Attack on Titan':
        print('Count:', resp.text.count('img'))
        return resp.text.count('img') > 20
