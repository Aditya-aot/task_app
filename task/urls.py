from django.urls import path
from . import views
from task.views import home

urlpatterns = [
    path('', views.home , name='home') 

]