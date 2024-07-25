from django.urls import path
from account import views


urlpatterns = [
    path('', views.account_settings, name='account'),
    path('login/', views.login_func, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('signup/', views.signup_func, name='signup_user'),
]
