from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('dekho',views.dekho,name='dekho'),
    path('remove/<int:pk>',views.remove,name='remove'),
    ]