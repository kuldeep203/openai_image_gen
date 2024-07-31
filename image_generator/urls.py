# image_generator/urls.py

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import image_generator_view

urlpatterns = [
                  path('', image_generator_view, name='image_generator'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
