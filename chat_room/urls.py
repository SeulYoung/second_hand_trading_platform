from django.urls import path
from . import views

urlpatterns = [
    path('temp/', views.tem, name="tem"),
    path('chatRoom/', views.chat_room, name="chatRoom"),
]
