from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('details/', views.details, name="details"),
    path('upload/', views.upload_commodity, name='upload'),
] + static(settings.MEDIA_URL, docunment_root=settings.MEDIA_ROOT)
