from django.urls import path
from .views import ImageGenerationView

urlpatterns = [
    path("", ImageGenerationView.as_view(), name="Image_list"),
]
