
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # or your actual view endpoints
]
