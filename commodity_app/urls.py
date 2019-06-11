from django.urls import path
from . import views

urlpatterns = [
    path('details/', views.details, name="details"),
    path('upload/', views.upload_commodity, name='upload'),
]
