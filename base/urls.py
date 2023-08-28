from django.urls import path
from base import views


urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('author/', views.author, name='author'),
    path('404/', views.test_404, name='test_404'),
]
