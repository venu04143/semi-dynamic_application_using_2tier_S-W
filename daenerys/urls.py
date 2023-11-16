from django.urls import path
from daenerys.views import *
app_name='nothing'

urlpatterns=[
    path('dany/',dany,name='dany')
]