from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView ,name="home"),
    path('<str:room>/', views.roomView, name="room"),
    path('checkView', views.checkView, name="check"),
    path('send', views.sendView, name="send"),
    path('getMessages/<str:room>/', views.getMessages, name="getMessages"),
]




