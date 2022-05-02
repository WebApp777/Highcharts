from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('random_data', get_random_data)
]
