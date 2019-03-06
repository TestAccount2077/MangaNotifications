from .models import *

from .utils import *


def dispatch_notifications():
    
    for manga in Manga.objects.all():
        
        released = scan_site(manga.name, manga.url)
        
        if released:
            
            manga.upcoming_chapter += 1
            manga.save()
                        
            for subscriber in manga.subscribers.all():
                
                retries = 3
                
                while retries:
                    
                    subject = f'{ manga.name } Chapter { manga.upcoming_chapter } is out!'
                    body = manga.url
                    
                    sent = send_email(subscriber.email, subject, body)
                    
                    if sent is True:
                        break
                    
                    retries -= 1
