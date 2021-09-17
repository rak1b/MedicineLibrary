from os import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import homeView,detailsView,testView,searchView,signupView,loginView
urlpatterns = [
    path('',homeView,name='homeView'),
    path('details/<uuid:id>/<str:name>',detailsView,name='detailsView'),
    path('search',searchView,name='searchView'),
    path('signup',signupView,name='signupView'),
    path('login',loginView,name='loginView'),
    path('test',testView,name='testView'),
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)