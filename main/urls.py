from django.conf.urls import url
from .views import *

app_name = 'main'

urlpatterns = [

    # HTTP URLs
    url(r'^$', index),

    # AJAX URLs
    url(r'^ajax/register-email/$', register_email),

]
