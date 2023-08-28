from django.urls import path
from xChannel import views


urlpatterns = [
    path('', views.channel, name='xChannel'),
    path('my_messages/', views.my_messages, name='my_messages'),
]
