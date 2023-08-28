from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from API import views


urlpatterns = [
    path('messages/', views.message_list),
    path('messages/<int:pk>/', views.message_detail),
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
