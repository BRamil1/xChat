from django.urls import path
from xChannel import views


urlpatterns = [
    path('', views.channel, name='xChannel'),
    path('my_messages/', views.my_messages, name='my_messages'),
    path('create/', views.create, name='create'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('delete_all/', views.delete_all, name='delete_all'),
]
