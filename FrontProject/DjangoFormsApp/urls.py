from django.urls import path
from .views import *



urlpatterns=[
    path("",index,name='index'),
    path('update/',form_name,name='form_name'),
]