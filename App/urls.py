from os import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import homeView,detailsView
urlpatterns = [
    path('',homeView,name='homeView'),
    path('details/<uuid:id>',detailsView,name='detailsView'),
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)