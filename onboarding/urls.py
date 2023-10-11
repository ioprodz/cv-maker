from django.urls import path
from .views import *

urlpatterns = [
   path('', home),
   path('onboarding', onboarding),
   path('onboarding/<int:step>', onboardingStep),
]
