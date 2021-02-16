from django.urls import path
from .views import *

urlpatterns = [
    path('contact', contacts, name="contacts")
]