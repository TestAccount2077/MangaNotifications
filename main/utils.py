import os
import sendgrid
import requests

from sendgrid.helpers.mail import *

def send_email(email, subject, body):
    
    try:
        os.environ['SENDGRID_API_KEY'] = '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'
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

        from_email = Email("do_not_reply")
        to_email = Email(email)

        content = Content("text/plain", body)

        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        
        return True
    
    except Exception as e:
        
        return 'Email sending failed'
    
def scan_site(name, url):
    
    resp = requests.get(url)
    
    if name == 'Attack on Titan':
        return resp.text.count('img') > 20
