"""
URL configuration for xChat project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls'), name='main'),  # main site
    path('account/', include('account.urls'), name='account'),  # everything related to the account
    path('channel/', include('xChannel.urls'),
         name='xChannel'),  # everything related to content processing and database
    path('admin/', admin.site.urls),  # everything related to the administrative control panel
    path('api/', include('API.urls'), name='xChannel'),  # everything related to API processing
]
