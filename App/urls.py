from os import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import homeView,detailsView,searchView,signupView,loginView,logoutView,forumView,askView,ques_detailsView
urlpatterns = [
    path('',homeView,name='homeView'),
    path('details/<uuid:id>/<str:name>',detailsView,name='detailsView'),
    path('search',searchView,name='searchView'),
    path('signup',signupView,name='signupView'),
    path('login',loginView,name='loginView'),
    path('logout',logoutView,name='logoutView'),
    path('forum',forumView,name='forumView'),
    path('ask',askView,name='askView'),
    path('quesdetails/<int:id>',ques_detailsView,name='ques_detailsView'),
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)