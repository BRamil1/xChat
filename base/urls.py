from django.urls import path
from base import views


urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
]
