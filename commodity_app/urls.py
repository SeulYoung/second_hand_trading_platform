from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
                  path('details/', views.details, name="details"),
                  path('buy/', views.buy, name="buy"),
                  path('upload/', views.upload_commodity, name='upload'),
                  path('favorites/', views.favorites, name="favorites"),
                  path('order/', views.order, name="order"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
