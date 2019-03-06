from django.shortcuts import render
from django.http import JsonResponse
from django.core.validators import validate_email

from rest_framework import status

from .models import *

import json



def index(request):
    
    context = {
        'mangas': Manga.objects.all()
    }
    
    return render(request, 'main/index.html', context=context)


def register_email(request):
    
    if request.is_ajax():
        
        data = request.GET
        
        email = data['email']
        mangas = json.loads(data['mangas'])
        
        try:
            validate_email(email)
            
        except Exception as e:
            
            return JsonResponse(
                {
                    'error': 'This email is invalid'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        subscriber, created = Subscriber.objects.get_or_create(email=email)
        
        mangas = Manga.objects.filter(name__in=mangas)
        
        subscriber.mangas.set(mangas, clear=True)
        
        return JsonResponse({
            'created': created
        })
