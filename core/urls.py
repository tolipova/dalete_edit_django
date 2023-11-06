from django.urls import path
from .views import *
urlpatterns = [
    path('company/', company, name='company'),
    path('delete/<uuid:id>', delete, name='post'),
    path('edit/<uuid:id', edit, name='post'),
    path('edit/editrecord/<uuid:id>', editrecord, name='post')
]
