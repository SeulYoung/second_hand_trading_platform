from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
                  path('details/', views.details, name="details"),
                  path('buy/', views.buy, name="buy"),
                  path('create_order/', views.create_order, name="create_order"),
                  path('upload/', views.upload_commodity, name='upload'),
                  path('favorites/', views.favorites, name="favorites"),
                  path('order/', views.order, name="order"),
                  path('order_content/', views.order_info, name="order_content"),
                  path('deal_confirm/', views.deal_confirm, name="deal_confirm"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
