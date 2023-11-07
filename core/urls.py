from django.urls import path
from .views import *
urlpatterns = [
    path('', company , name='company'),
    path('add', add, name='post'),
    path('delete/<uuid:id>', delete, name='post'),
    path('edit/<uuid:id>', edit, name='post'),
    path('edit/editrecord/<uuid:id>', editrecord, name='post')
]
