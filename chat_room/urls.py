from django.urls import path
from . import views

urlpatterns = [
    path('temp/', views.tem, name="index"),
    path('chatRoom/', views.chat_room, name="index"),
]
