from django.urls import path
from aegon.views import *
app_name='nothing'

urlpatterns=[
    path('jonsnow/',jonsnow,name='jonsnow')
]