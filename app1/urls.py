from django.urls import path
from app1.views import *

app_name='app1'

urlpatterns=[
    path('app1_function/',app1_function,name='app1_function'),

]
