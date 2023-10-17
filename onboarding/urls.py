from django.urls import path
from .views import *

app_name = 'onboarding'

urlpatterns = [
   path('', home),
   path('onboarding/', ContactWizard.as_view(), name='forms'),
   
]
