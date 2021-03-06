from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
    path('switch/', views.switch, name="switch"),
    path('logout/', views.logout, name="logout"),
    path('sellerhome/', views.sellerhome, name="sellerhome"),
    path('personalinf/', views.personalinf, name="personalinf"),
    path('exchange/', views.exchange, name="exchange"),
    path('password_update/', views.password_update, name="password_update"),

]
