#from django.contrib.auth.views import logout
from django.urls import path
from . import views

#<link type="text/css" rel="stylesheet" href="{% static 'css/materialize.min.css' %}"  media="screen,projection"/>
 #       <link type="text/css" rel="stylesheet" href="{% static 'css/style.css' %}"  media="screen,projection"/>


urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>/', views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register_view, name='register'),
    
]
