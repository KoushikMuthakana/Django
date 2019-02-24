from django.urls import  path
from .views import *

urlpatterns=[
path('',index,name='lifeappindex'),
path('re/',renindex,name='renderindex')


]
    

