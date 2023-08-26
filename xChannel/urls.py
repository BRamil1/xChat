from django.urls import path
from xChannel import views


urlpatterns = [
    path('', views.channel, name='xChannel'),
]
