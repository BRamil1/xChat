from django.urls import path
from main import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('author/', views.author, name='author'),
]
