from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
    path('switch/', views.switch, name="switch"),
    path('logout/', views.logout, name="logout"),
    path('sellerhome/', views.sellerhome, name="sellerhome"),

]
