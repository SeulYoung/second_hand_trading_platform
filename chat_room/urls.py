from django.urls import path
from . import views

urlpatterns = [
    path('chatRoom/', views.chat_room, name="chatRoom"),
]
