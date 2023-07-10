from django.urls import path
from . import views

app_name = 'Reader'
urlpatterns = [
    path('', views.index, name='index'),
]