from django.urls import path, include
from .views import *

app_name = 'myapp'
urlpatterns = [
    path('',      top,         name='view_top'),
    path('add/',  add_person,  name='view_add_person'),
]
